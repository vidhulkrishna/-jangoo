from django.urls import path
from .import views

urlpatterns=[
    path('msg/',views.message),
    path('sample.html/',views.sample)
    
]