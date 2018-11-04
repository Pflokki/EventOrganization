from django.shortcuts import render

from django.http import HttpResponse, HttpRequest


def show_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'main_page.html')
