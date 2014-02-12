from django.shortcuts import render
from x_for_y.models import SiteTrafficTracker

# Create your views here.

traffic_tracker = SiteTrafficTracker()

def index(request):
    traffic_tracker.increment_visited()
    traffic_tracker.save()

    return render(request, "index.html", {
        'tracker' : traffic_tracker
    })