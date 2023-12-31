from django.shortcuts import render, redirect
from .models import Scheduler, Medic

from datetime import datetime, timedelta
import calendar
import json

# Create your views here.


def homeView(request):
    context = {}
    print(f"Metoda pe homeView este: ->{request.method}<- ")
    if request.method == "GET":
        context.update(handleDates(request))

    if request.method == "POST":
        context.update(handleScheduler(request))
        
    return render(request, 'home.html', context=context)

def schedulerView(request):

    print(f"Metoda pe schedulerView este: ->{request.method}<- ")

    context = {}

    if request.method == "GET":
        context.update(handleDates(request))
        context.update(handleMedicCards(request))

    if request.method == "POST":
        print("Request POST: ")
        if request.headers.get('action') == 'save':
            saveScheduler(request)
            return redirect('home')
        else:
            context.update(handleScheduler(request))
            context.update(handleMedicCards(request))
    
    return render(request, "scheduler.html", context)

def saveScheduler(request):
    print("SAVE SCHEDULER")
    decodedData = json.loads(request.body.decode("utf-8"))
    print(decodedData)
    for element in decodedData:
        date = datetime.strptime(element, '%d-%m-%Y')
        tura1 = getMedic(decodedData[element][0])
        tura2 = getMedic(decodedData[element][1])
        tura3 = getMedic(decodedData[element][2])
        record = Scheduler(date=date, tura1=tura1, tura2=tura2, tura3=tura3)
        record.save()

    print()

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


def handleMedicCards(request):
    medicList = Medic.objects.all()
    return {"medicList": medicList}