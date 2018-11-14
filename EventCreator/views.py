from django.shortcuts import render, redirect
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


s_field_list = ['event', 'event_location', 'location_address', 'decoration', 'artist_class', 'artist', 'result']
context_list = [
    ("Тип события", Event),
    ("Место проведения", EventLocation),
    ("Адрес", LocationAddress),
    ("Украшение", Decoration),
    ("Тип артиста", ArtistClass),
    ("Артист", Artist),
]


def show_creator(request: HttpRequest, page_name: str) -> HttpResponse:

    if (request.method == "GET" or page_name not in s_field_list) and page_name != s_field_list[0]:
        raise Http404
        # if page_name in s_field_list:
        #     return render(request, 'main_page.html')
        # else:
        #     raise Http404

    else:
        page_index = s_field_list.index(page_name)

        prev_form_value = int(request.POST['r-item']) if 'r-item' in request.POST.keys() else -1
        if page_index != 0 and request.method == "POST":
            request.session[s_field_list[page_index - 1]] = prev_form_value
        if page_index == len(s_field_list) - 1:
            return redirect('/event-created')
        try:
            content_title, context_cls = context_list[page_index]
            if page_index == 0:
                items = context_cls.get_list()
            else:
                items = context_cls.get_list(prev_form_value)

            context = {
                'page_title': content_title,
                'items': items,
                'next_button_enable': "disabled" if len(items) != 0 else "",
                'description': "Выберите один из вариантов" \
                    if len(items) != 0 else "В заявленной категории нечего выбрать",
                'next_page_url': s_field_list[page_index + 1] if page_index + 2 != len(s_field_list) else 'result'
            }
            return render(request, 'event_creator.html', context=context)

        except IndexError:
            raise Http404


def show_personal_info(request: HttpRequest) -> HttpResponse:
    result_context_list = []
    result_context = {}

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

    result_context['form'] = form
    result_context['excluded_date'] = ['2018-11-6', '2018-11-7', '2018-11-8']
    return render(request, 'result.html', context=result_context)


def show_success(request: HttpRequest) -> HttpResponse:
    return render(request, 'success.html')
