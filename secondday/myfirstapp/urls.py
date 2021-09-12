from django.urls import path
from myfirstapp import views

urlpatterns = [
    path("new/",views.welcome)
]