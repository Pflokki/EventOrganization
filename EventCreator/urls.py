from django.urls import path

from . import views

urlpatterns = [
    path("event-creator", views.show_creator),
    path("event-created", views.show_personal_info),
    # path("event-success", views.show_succes),
]
