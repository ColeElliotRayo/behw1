from django.urls import path

from apps.core import views

urlpatterns = [
    path('', views.home, name='home'),
    path('chart/', views.chart, name='chart'),
    path('graph/', views.graph, name='graph'),
]
