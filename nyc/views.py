from django.shortcuts import render
from django.views import View

from nyc.boroughs import boroughs


class CityView(View):
    def get(self, request):
        return render(request=request, template_name='city.html', context={'boroughs': boroughs.keys()})


class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )


class ActivityView(View):                                           
   def get(self, request, borough, activity):
       return render(
           request=request,
           template_name='activity.html',
           context={'borough': borough, 'activity': activity, 
                    'venues': boroughs[borough][activity].keys()
                   }
       ) # Defines the Class ActivityView, Requests the available activities from the boroughs.py file,
         # retuns the information so it can be passed forward to the webpage.


class VenueView(View):
    def get(self, request, borough, activity, venue):
        return render(
            request=request,
            template_name='venue.html',
            context={'borough': borough,
                     'venue': venue,
                     'description': boroughs[borough][activity][venue]
                     ['description']
                    }
        )   # Defines the Class VenueView, Requests the venue information from the bouroughs.py file,
            # retuns the information so it can be passed forward to the webpage.
  