from django.shortcuts import render, HttpResponseRedirect
from xfory.models import SiteTrafficTracker, PotentialMember

# Create your views here.

if not SiteTrafficTracker.objects.all()[0]:
    traffic_tracker = SiteTrafficTracker()
    traffic_tracker.save()
else:
    traffic_tracker = SiteTrafficTracker.objects.all()[0]

def index(request):
    traffic_tracker.increment_visited()
    traffic_tracker.save()

    return render(request, "index.html", {
        'tracker' : traffic_tracker
    })

def sign_up(request):
    if request.POST:
        name = request.POST.get('name')
        email = request.POST.get('email')

        new_member = PotentialMember(name=name, email=email)
        new_member.save()
        traffic_tracker.increment_splash()
        traffic_tracker.save()
        
        print request.POST
    
    return HttpResponseRedirect('/')