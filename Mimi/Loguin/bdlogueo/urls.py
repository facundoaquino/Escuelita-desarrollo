from django.urls import path
from . import views

urlpatterns = [
    path("loguin", views.loguin),
    path("ingresarUs",views.ingresarUs),
]