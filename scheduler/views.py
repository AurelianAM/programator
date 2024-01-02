from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Scheduler, Medic

from datetime import datetime, timedelta
import calendar
import json

# Create your views here.


def homeView(request):
    context = {}
    if request.method == "GET":
        context.update(handleDates(request))
    if request.method == "POST":
        context.update(handleScheduler(request))
    return render(request, 'home.html', context=context)

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

def mediciView(request):
    context = {}
    if request.method == "GET":
        context.update(handleMedicList(request))
    elif request.method == "POST":
        if "modifiedNickname" in request.POST:
            context.update(handleModifyMedic(request))
        elif "newNickname" in request.POST:
            context.update(handleAddNewMedic(request))
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
    except Medic.unique_error_message:
        return {"status" : "Medic with provided nickname already exists"}

def handleModifyMedic(request):
    id = int(request.POST.get("actualMedicId"))
    modifiedNickname = request.POST.get("modifiedNickname")
    modifiedFirstName = request.POST.get("modifiedFirstName")
    modifiedLastName = request.POST.get("modifiedLastName")

    medic = Medic.objects.get(id=id)
    try:
        medic.nickname = modifiedNickname
        medic.firstName = modifiedFirstName
        medic.lastName = modifiedLastName
        medic.save()
        return {"status" : "Medic modified successfully"}
    except Medic.unique_error_message:
        return {"status" : "Medic with provided nickname already exists"}

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
    startDate = f"{datetime.now().year}-{datetime.now().month}-{1:02d}"
    endDate = f"{datetime.now().year}-{datetime.now().month}-{calendar.monthrange(datetime.now().year, datetime.now().month)[1]:02d}"
    return {"status" : "ok GET - handle Dates", "startDate" : startDate, "endDate" : endDate}

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
        try:
            record = Scheduler.objects.get(date=date)
            t1 = record.tura1 if record.tura1 else ''
            t2 = record.tura2 if record.tura2 else ''
            t3 = record.tura3 if record.tura3 else ''
            scheduler[strDate] = {
                'tura1': t1,
                'tura2': t2,
                'tura3': t3}
        except Scheduler.DoesNotExist:
            scheduler[strDate] = {
                'tura1': '',
                'tura2': '',
                'tura3': ''}
    return {"scheduler" : scheduler, "status" : "ok POST - handle Scheduler", "startDate" : startDate, "endDate" : endDate}


def handleMedicList(request):
    medicList = Medic.objects.all()
    return {"medicList": medicList}