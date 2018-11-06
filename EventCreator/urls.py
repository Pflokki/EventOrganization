from django.urls import path

from . import views

urlpatterns = [
    path("event-creator/<str:page_name>", views.show_creator),
    path("event-created", views.show_personal_info),
    # path("event-success", views.show_succes),
]
