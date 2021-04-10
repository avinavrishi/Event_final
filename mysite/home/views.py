from django.shortcuts import render
from .models import Events
from news.models import News

#Home page view
def HomeView(request):
        Event = Events.objects.all()
        News_cont = News.objects.all()

        params = {'Eventss': Event, 'Newss': News_cont}


        return render(request,'home/home.html', params )

#Event page View
def EventView(request):

    allEvents=[]
    allEvent =  Events.objects.values('Event_type','Event_id')
    evt = { item['Event_type'] for item in allEvent }
    for ev in evt:
        x = Events.objects.filter(Event_type=ev)
        allEvents.append([x])


    params = {'allEvents':allEvents}

    return render(request,'home/event.html', params)

def EventDetailView(request,id):
    Event = Events.objects.filter(Event_id=id)
    params = {'Event': Event}

    return render(request,'home/Event_detail_page.html', params)


#About page View
def AboutView(request):
    return render(request,'home/about_page.html')


#Contact page View
def ContactView(request):
    return render(request,'home/contact_page.html')
