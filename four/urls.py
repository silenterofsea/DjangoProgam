from django.urls import path
from . import views


app_name = 'four'
urlpatterns = [
    path('', views.index, name='index'),
]
