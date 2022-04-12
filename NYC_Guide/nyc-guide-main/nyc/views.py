from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
#View rendered for '<str:borough>/<str:activity>' in url.py
    def get(self, request):
        return render(
            request=request,
            # render city.html page
            template_name='city.html', 
            # send html context for display or use 
            context={'boroughs': boroughs.keys()}
        )


class BoroughView(View):
#View rendered for '<str:borough>/<str:activity>' in url.py
    def get(self, request, borough):
        return render(
            request=request,
            # render city.html page
            template_name='borough.html', 
            # send html context for display or use 
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )

class ActivityView(View):
#View rendered for '<str:borough>/<str:activity>' in url.py
# The borough and activity arguments are strings taken from the URL
    def get(self, request, borough, activity):
        return render(
            request=request,
            # render city.html page
            template_name='activity.html', 
            # send html context for display or use; context is a dictionary which is passed to render and will be available in the template
            context={ 'borough': borough,'activity': activity, 'activities': boroughs[borough][activity].keys()}
        )


class VenueView(View):
#View rendered for '<str:borough>/<str:activity>' in url.py
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            # send html context for display or use 
            template_name='venue.html', 
            # send html context for display or use 
            context={'borough': borough,'activity': activity, 'venue': venue, 'description': boroughs[borough][activity][venue].get("description")}
        )
