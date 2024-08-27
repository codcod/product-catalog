# pylint: disable=C0114,C0115,C0116
from django.urls import path

from . import views

urlpatterns = [
    path('projects', views.index, name='index'),
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    path('journey/<int:journey_id>/', views.journey_detail, name='journey_detail'),
]
