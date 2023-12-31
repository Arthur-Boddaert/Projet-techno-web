from django.urls import path

from . import views

urlpatterns = [
    #path("", views.index, name="appli-index"),
    path('', views.formulaire, name="formulaire")
]