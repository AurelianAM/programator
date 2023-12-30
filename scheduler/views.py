from django.shortcuts import render
from .models import Scheduler, Medic

from datetime import datetime, timedelta
import calendar

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

    if "dataToSave" in request.POST:
        print("DataToSave: ", request.POST['dataToSave'])

    print(f"Metoda pe schedulerView este: ->{request.method}<- ")

    context = {}

    if request.method == "GET":
        context.update(handleDates(request))
        context.update(handleMedicCards(request))

    if request.method == "POST":
        context.update(handleScheduler(request))
        context.update(handleMedicCards(request))
    
    return render(request, "scheduler.html", context)

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