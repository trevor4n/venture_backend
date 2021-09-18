# from django.shortcuts import render, redirect
from .models import Trip, Guideline, Restriction, Airline

# Django REST Framework
from .serializers import TripSerializer, GuidelineSerializer 
from rest_framework import generics

# icebox - Section Django REST Article
# from rest_framework import viewsets

# Django REST Framework - JSONN Responses in Django
from django.http import JsonResponse

import requests
import os

# def trip_list(req):
#     trips = Trip.objects.all()
#     return render(req, 'venture/trip_list.html', {'trips': trips})

# def trip_detail(req, pk):
#     try:
#         trip = Trip.objects.get(id=pk)
#     except:
#         trip = {
#             'name': 'No trip found',
#             'destination':  f'with id {pk}' # fix - destination ? id ?
#         }
#         print(f"trip with id={pk} didn't work")
#     return render(req, 'venture/trip_detail.html', {'trip': trip})

# def trip_create(req):
#     if req.method == 'POST':
#         form = TripForm(req.POST)
#         if form.is_valid():
#             trip = form.save()
#             return redirect('trip_detail', pk=trip.pk)
#     else:
#         form = TripForm()
#     return render(req, 'venture/trip_form.html', {'form': form})

# def trip_edit(req, pk):
#     trip = Trip.objects.get(pk=pk)
#     if req.method == 'POST': # html forms are limited to POST & GET w/o s/t s/a fetch
#         form = TripForm(req.POST, instance=trip)
#         if form.is_valid():
#             trip = form.save()
#             return redirect('trip_detail', pk=trip.pk)
#     else:
#         form = TripForm(instance=trip)
#     return render(req, 'venture/trip_form.html', {'form': form})

# def trip_delete(req, pk):
#     Trip.objects.get(id=pk).delete()
#     return redirect('trip_list')

# Django REST Framework
# def guideline_detail(req, pk):
#     try:
#         guideline = Guideline.objects.get(id=pk)
#     except:
#         guideline = {
#             'location': 'No guideline found',
#             # 'destination':  f'with id {pk}' # fix - destination ? id ?
#         }
#         print(f"guideline with id={pk} didn't work")
#     return render(req, 'venture/guideline_detail.html', {'guideline': guideline})

# Django REST Framework
class TripList(generics.ListCreateAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class TripDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer

class GuidelineList(generics.ListCreateAPIView):
    queryset = Guideline.objects.all()
    serializer_class = GuidelineSerializer

class GuidelineDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Guideline.objects.all()
    serializer_class = GuidelineSerializer

# icebox - Section Django REST Article
# class TripView(viewsets.ModelViewSet):  
#     serializer_class = TripSerializer   
#     queryset = Trip.objects.all()     

searchOptions = {
    'apiVersion': '1',
    'key': os.environ['TRAVEL_SAFE_KEY'],
    'prodKey': os.environ['TRAVEL_SAFE_KEY_PROD'],
    'baseUrl': 'https://sandbox.travelperk.com',
    # 'baseUrl': 'https://api.travelperk.com',
    'api': '/travelsafe',
    # icebox - https://developers.travelperk.com/docs/rest-api
    # endpoint: '/restrictions',
    # endpoint: '/airline_safety_measures',
    'endpoint': '/guidelines'
}

# searchParams = {
#     'locationType': "country_code",
#     'location': "" + event.target.value
# }

def proxy(req, lt, loc):
    # stretch - Travel Restrictions parametric url
    # ref - https://developers.travelperk.com/docs/travel-restrictions
    # stretch - Airline Safety Measurres parametric url
    # ref - https://developers.travelperk.com/docs/airline-safety-measures
    # wip - Travel Guidelines parametric url
    # ref - https://developers.travelperk.com/reference#retrieve-a-local-guideline
    pURL = f"{searchOptions['baseUrl']}{searchOptions['api']}{searchOptions['endpoint']}?location_type={lt}&location={loc}"

    pHeaders = {
        # 'Authorization': 'ApiKey ' + os.environ['TRAVEL_SAFE_KEY'],
        'Authorization': 'ApiKey ' + searchOptions['key'],
        # 'Authorization': 'ApiKey ' + searchOptions['prodKey'],
        'Accept': 'application/json',
        'Api-Version': '1',
        'Accept-Language': 'en'
    }

    try:
        # r = requests.get(url='https://www.thecolorapi.com/id?hex=FFFF00')
        # print('req')
        # print(pretty_request(req))
        r = requests.get(url=pURL, headers=pHeaders)
        data = r.json()
        print(r.status_code)
        # print(data)
        return JsonResponse(data, safe=False)
    except requests.exceptions.HTTPError as errh:
        print(errh)
    except requests.exceptions.ConnectionError as errc:
        print(errc)
    except requests.exceptions.Timeout as errt:
        print(errt)
    except requests.exceptions.RequestException as err:
        print(err)

# ref - https://gist.github.com/defrex/6140951
def pretty_request(request):
    headers = ''
    for header, value in request.META.items():
        if not header.startswith('HTTP'):
            continue
        header = '-'.join([h.capitalize() for h in header[5:].lower().split('_')])
        headers += '{}: {}\n'.format(header, value)

    return (
        '{method} HTTP/1.1\n'
        'Content-Length: {content_length}\n'
        'Content-Type: {content_type}\n'
        '{headers}\n\n'
        '{body}'
    ).format(
        method=request.method,
        content_length=request.META['CONTENT_LENGTH'],
        content_type=request.META['CONTENT_TYPE'],
        headers=headers,
        body=request.body,
    )