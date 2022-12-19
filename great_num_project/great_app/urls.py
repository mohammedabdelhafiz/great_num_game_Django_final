from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('validate', views.validate),	   

]