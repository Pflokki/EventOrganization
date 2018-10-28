from django.shortcuts import render

from django.http import HttpResponse, HttpRequest


def show_page(request: HttpRequest):
    return render(request, 'event_creator.html')
