from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, Http404

from .models import Event, EventLocation, LocationAddress, Decoration, ArtistClass, Artist, OrderInfo
from .forms.personal_info_form import PersonalInfoForm


def get_event() -> dict:
    context = {
        'page_title': "Event",
        'description': "Choose event",
        'items': Event.get_list()
    }

    return context


s_field_list = ['event', 'event_location', 'location_address', 'decoration', 'artist_class', 'artist']
context_list = [
    ("Тип события", Event),
    ("Место проведения", EventLocation),
    ("Адрес", LocationAddress),
    ("Украшение", Decoration),
    ("Тип артиста", ArtistClass),
    ("Артист", Artist),
]


def show_creator(request: HttpRequest) -> HttpResponse:
    print(f"POST: {request.POST.values()}")
    print(f"SESSION:")
    for k in request.session.keys():
        print(f"{k}: {request.session[k]}")

    if request.method == "GET":
        request.session['index'] = 0

    index = request.session['index']

    if request.method == "POST":
        request.session[s_field_list[index]] = request.POST['r-item']
        index += 1
        if index >= len(s_field_list):
            request.method = "GET"
            return show_personal_info(request)
            request.session['index'] = 0

        request.session['index'] = index

    try:
        content_title, context_cls = context_list[index]
        if index == 0:
            context_dict = context_cls.get_list()
        else:
            context_dict = context_cls.get_list(int(request.session[s_field_list[index - 1]]))
    except KeyError:
        raise Http404

    try:
        if index == len(context_list):
            return render(request, 'main_page.html')
        else:
            context = {
                'page_title': content_title,
                'description': "Выберите один из вариантов",
                'items': context_dict,
            }
    except IndexError:
        request.session['index'] = 0
        raise Http404

    return render(request, 'event_creator.html', context=context)


def show_personal_info(request: HttpRequest) -> HttpResponse:
    print(f"POST: {request.POST.values()}")
    result_context_list = []
    result_context = {}
    try:
        for ci in context_list:
            result_context_list.append({
                'header': ci[0],
                'desc': ci[1].get_first(request.session[s_field_list[len(result_context_list)]])['desc'],
                'price': ci[1].get_first(request.session[s_field_list[len(result_context_list)]])['price'],
            })
        result_context['items'] = result_context_list
    except:
        raise Http404

    if request.method == "POST":
        form = PersonalInfoForm(request.POST)
        if form.is_valid() \
                and 'event' in request.session.keys() \
                and 'location_address' in request.session.keys() \
                and 'decoration' in request.session.keys() \
                and 'artist' in request.session.keys():
            OrderInfo.save_record(
                p_first_name=request.POST['p_first_name'],
                p_last_name=request.POST['p_last_name'],
                p_phone=request.POST['p_phone'],
                p_email=request.POST['p_email'],
                event_time=request.POST['event_time'],

                id_event=request.session['event'],
                id_location_address=request.session['location_address'],
                id_decoration=request.session['decoration'],
                id_artist=request.session['artist']
            )
            return render(request, 'success.html')
    else:
        form = PersonalInfoForm()

    result_context['form'] = form
    result_context['excluded_date'] = ['2018-11-6', '2018-11-7', '2018-11-8']
    return render(request, 'result.html', context=result_context)


def show_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'success.html')
