from django.urls import path
from . import views
# styling
# from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

urlpatterns = [
    # path('', views.trip_list, name='trip_list'), 
    # path('guidelines/', views.guideline_list, name='guideline_list'), 
    # path('trips/<int:pk>', views.trip_detail, name='trip_detail'),
    # path('guidelines/<int:pk>', views.guideline_detail, name='guideline_detail'),
    # path('trips/new', views.trip_create, name='trip_create'),
    # path('trips/<int:pk>/edit', views.trip_edit, name='trip_edit'),
    # path('trips/<int:pk>/delete', views.trip_delete, name='trip_delete'),
    
    path('trips/', views.TripList.as_view(), name='trip_list'),
    path('trips/<int:pk>', views.TripDetail.as_view(), name='trip_detail'),
    path('guidelines/', views.GuidelineList.as_view(), name='guideline_list'),
    path('guidelines/<int:pk>', views.GuidelineDetail.as_view(), name='guideline_detail'),
    path('proxy/',views.proxy)
]