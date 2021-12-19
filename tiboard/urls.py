from django.urls import path
from . import views

app_name = 'tiboard'

urlpatterns = [
    path('', views.index, name='index'),
]
