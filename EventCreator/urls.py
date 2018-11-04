from django.urls import path

from . import views

urlpatterns = [
    path("event-creator", views.show_page),
]
