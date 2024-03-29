from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Scheduler, Medic

from datetime import datetime, timedelta
import calendar
import json

# Create your views here.
RO_MONTHS = {
    1 : "Ianuarie",
    2 : "Februarie",
    3 : "Martie",
    4 : "Aprilie",
    5 : "Mai",
    6 : "Iunie",
    7 : "Iulie",
    8 : "August",
    9 : "Septembrie",
    10 : "Octombrie",
    11 : "Noiembrie",
    12 : "Decembrie"
}
RO_WEEKDAYS = {
    0 : "Luni",
    1 : "Marti",
    2 : "Miercuri",
    3 : "Joi",
    4 : "Vineri",
    5 : "Sambata",
    6 : "Duminica"
}

def homeView(request):
    context = {}
    if request.method == "GET":
        context.update(handleDates(request))        
    if request.method == "POST":
        context.update(handleScheduler(request))
    if request.user.is_authenticated:
        return render(request, 'home.html', context=context)
    else:
        return redirect('myLogin')
    
@login_required
def schedulerView(request):
    context = {}
    if request.method == "GET":
        context.update(handleDates(request))
        context.update(handleMedicList(request))
    if request.method == "POST":
        if request.headers.get('action') == 'save':
            saveScheduler(request)
            return redirect('scheduler')
        else:
            context.update(handleScheduler(request))
            context.update(handleMedicList(request))
    return render(request, "scheduler.html", context)

@login_required
def mediciView(request):
    context = {}
    if request.method == "GET":
        context.update(handleMedicList(request))
    elif request.method == "POST":
        if "modifiedNickname" in request.POST:
            context.update(handleModifyMedic(request))
        elif "newNickname" in request.POST:
            context.update(handleAddNewMedic(request))
        elif "delete" in request.headers.get('action'):
            context.update(handleDeleteMedic(request))
        return redirect('medici')
    return render(request, "medici.html", context=context)

def handleAddNewMedic(request):
    newNickname = request.POST.get("newNickname")
    newFirstName = request.POST.get("newFirstName")
    newLastName = request.POST.get("newLastName")
    newMedic = Medic(nickname=newNickname, firstName=newFirstName, lastName=newLastName)
    try:
        newMedic.save()
        return {"status" : "Medic added successfully"}
    except Exception as e:
        print(e)
        return {"status" : "Medic with provided nickname already exists"}

def handleModifyMedic(request):
    id = int(request.POST.get("actualMedicId"))
    modifiedNickname = request.POST.get("modifiedNickname")
    modifiedFirstName = request.POST.get("modifiedFirstName")
    modifiedLastName = request.POST.get("modifiedLastName")
    # print("Id-ul medicului care trebuie modificat: ", id)

    medic = Medic.objects.get(id=id)
    try:
        print(medic)
        medic.nickname = modifiedNickname
        medic.firstName = modifiedFirstName
        medic.lastName = modifiedLastName
        medic.save()
        return {"status" : "Medic modified successfully"}
    except Exception as e: # Medic.unique_error_message:
        print(e)
        return {"status" : "Medic with provided nickname already exists"}

def handleDeleteMedic(request):
    id = int(request.body.decode("utf-8"))
    try:
        medic = Medic.objects.get(id=id)
        medic.delete()
        return {"status" : "Medic deleted successfully"}
    except Exception as e:
        print(e)
        return {"status" : "Error deleting medic"}

def saveScheduler(request):
    decodedData = json.loads(request.body.decode("utf-8"))
    for element in decodedData:
        date = datetime.strptime(element, '%d-%m-%Y')
        tura1 = getMedic(decodedData[element][0])
        tura2 = getMedic(decodedData[element][1])
        tura3 = getMedic(decodedData[element][2])
        record = Scheduler(date=date, tura1=tura1, tura2=tura2, tura3=tura3)
        record.save()
def getMedic(nickname):
    try:
        return Medic.objects.get(nickname=nickname)
    except Medic.DoesNotExist:
        return None   

def handleDates(request):
    startDate = f"{datetime.now().year}-{datetime.now().month:02d}-{1:02d}"
    endDate = f"{datetime.now().year}-{datetime.now().month:02d}-{calendar.monthrange(datetime.now().year, datetime.now().month)[1]-1:02d}"
    aDate = datetime.strptime(startDate, '%Y-%m-%d')+timedelta(days=3)
    ro_month = RO_MONTHS[aDate.month]
    return {"status" : "ok GET - handle Dates", "startDate" : startDate, "endDate" : endDate, "month" : ro_month, "year" : aDate.year}

def handleScheduler(request):
    scheduler = {}
    startDate = request.POST['start']
    endDate = request.POST['end']
    start = datetime.strptime(startDate, '%Y-%m-%d')
    end = datetime.strptime(endDate, '%Y-%m-%d')
    dates = [(start + timedelta(days=x))
                for x in range(0, (end - start).days+1)]
    for date in dates:
        strDate = date.strftime("%d-%m-%Y")
        # verify if date is weekend
        weekend = (date.weekday() == 5) or (date.weekday() == 6)
        try:
            record = Scheduler.objects.get(date=date)
            t1 = record.tura1 if record.tura1 else ''
            t2 = record.tura2 if record.tura2 else ''
            t3 = record.tura3 if record.tura3 else ''
            scheduler[strDate] = {
                'tura1': t1,
                'tura2': t2,
                'tura3': t3,
                'weekend': weekend}
        except Scheduler.DoesNotExist:
            scheduler[strDate] = {
                'tura1': '',
                'tura2': '',
                'tura3': '',
                'weekend': weekend}
    aDate = datetime.strptime(startDate, '%Y-%m-%d')+timedelta(days=3)
    ro_month = RO_MONTHS[aDate.month]
    return {"scheduler" : scheduler, "status" : "ok POST - handle Scheduler", "startDate" : startDate, "endDate" : endDate, "month" : ro_month, "year" : aDate.year}


def handleMedicList(request):
    medicList = Medic.objects.all()
    return {"medicList": medicList}