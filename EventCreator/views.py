from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

from .models import Event, EventLocation, LocationAddress, Decoration, ArtistClass, Artist


def get_event() -> dict:
    context = {
        'page_title': "Event",
        'description': "Choose event",
        'items': Event.get_list()
    }

    return context


def show_page(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        request.session['index'] = 0

    index = request.session['index']

    if request.method == "POST":
        index += 1
        request.session['index'] = index

    print(f"POST: {request.POST}")
    print(f"SESSION INDEX: {request.session['index']}")

    context_list = [
        ("Event", Event.get_list()),
        ("EventLocation", EventLocation.get_list()),
        ("LocationAddress", LocationAddress.get_list()),
        ("Decoration", Decoration.get_list()),
        ("ArtistClass", ArtistClass.get_list()),
        ("Artist", Artist.get_list()),
    ]

    try:
        context = {
            'page_title': context_list[index][0],
            'description': "Choose event",
            'items': context_list[index][1]
        }
    except IndexError:
        request.session['index'] = 0
        raise Http404

    return render(request, 'event_creator.html', context=context)
