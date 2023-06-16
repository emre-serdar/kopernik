# Created by Emre

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.renderUI),

    path('list/', views.SatelliteListAPI.as_view(), 
                        name='satellite-list'),

    path('create/', views.SatelliteCreateAPI.as_view(), 
                        name='satellite-create'),
    path('list/last-seven/', views.LastSevenSatellitesAPI.as_view(), name='last-seven-satellites')

]

# API ENDPOINTS:
# "localhost:8000/satellite"
# "localhost:8000/satellite/list"
# "localhost:8000/satellite/create"
# "localhost:800/satellite/list/last-seven"
