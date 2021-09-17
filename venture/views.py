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

# todo - Section Django REST Article
# class TripView(viewsets.ModelViewSet):  
#     serializer_class = TripSerializer   
#     queryset = Trip.objects.all()     


def proxy(req):
    r = requests.get(url='https://www.thecolorapi.com/id?hex=FFFF00')
    data = r.json()
    print(r.status_code)
    print(data)
    return JsonResponse(data, safe=False)