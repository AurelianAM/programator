from django.shortcuts import render
from .models import Scheduler, Medic

from datetime import datetime, timedelta
import calendar

# Create your views here.


def homeView(request):
    context = {}
    print(f"Metoda este: ->{request.method}<- ")
    context.update(handleScheduler(request))
    return render(request, 'home.html', context=context)

def schedulerView(request):
    context = {}
    context.update(handleScheduler(request))
    
    context.update(handleMedicCards(request))

    return render(request, "scheduler.html", context)

def handleScheduler(request):
    someContext = {}
    if request.method == 'POST':
        scheduler = {}
        someContext['status'] = 'ok POST'
        startDate = request.POST['start']
        endDate = request.POST['end']
        start = datetime.strptime(startDate, '%Y-%m-%d')
        end = datetime.strptime(endDate, '%Y-%m-%d')
        dates = [(start + timedelta(days=x))
                 for x in range(0, (end - start).days)]
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
        someContext['scheduler'] = scheduler
    elif request.method == 'GET':
        startDate = f"{datetime.now().year}-{datetime.now().month}-{1:02d}"
        endDate = f"{datetime.now().year}-{datetime.now().month}-{calendar.monthrange(datetime.now().year, datetime.now().month)[1]:02d}"
        print("Data de sfarsit: ", endDate)
        someContext['status'] = 'ok GET'
    someContext['startDate'] = startDate
    someContext['endDate'] = endDate
    
    return someContext


def handleMedicCards(request):
    medicList = Medic.objects.all()
    print(medicList)
    return {"medicList": medicList}