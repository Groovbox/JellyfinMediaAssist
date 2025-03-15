from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("new", views.new, name="new"),
    path("addsong", views.addsong, name="addsong"),
    path("api/lookup", views.lookup, name="lookup"),
]