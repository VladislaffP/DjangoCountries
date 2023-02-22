from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
from MainApp.models import Country
from MainApp.models import Language
from django.core.exceptions import ObjectDoesNotExist
import string
from django.core.paginator import Paginator

def home(request):
    context = {
        "pr_name": 'Проект DjangoCountries',
        "creator": "Паницкий В.В."
    }
    return render(request, 'index.html', context)


def countries_list(request):
#    with open('countries.json') as f:
#        cn = json.load(f)
    letters = string.ascii_uppercase;
    rq = request.GET
    lt = rq.get("start_letter");
    cn = Country.objects.all().order_by("country")

    letter_param = ''

    if lt:
    #    print(lt)
        cn = cn.filter(country__startswith=lt)
        letter_param = 'start_letter=' + lt + '&'

    #print(rq.get("start_letter"))
    paginator = Paginator(cn, 10)
    #print(paginator.object_list)
    page_number = rq.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    page_content = page_obj.object_list

    nums = list(range(1, paginator.num_pages+1))
    start_num = (int(page_number) - 1) * 10 + 1;
    context = {
        "cnts": cn,
        "letters": letters,
        'page': page_content,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'nums': nums,
        'letter_param': letter_param,
        'start_num': start_num
    }
    return render(request, 'countries-list.html', context)

def view_country(request, id):
    try:
        cnt = Country.objects.get(country=id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Страны с названием {id} не существует')

#    with open('countries.json') as f:
#        cn = json.load(f)
#    for c in cn:
#        if c['country'] == id:
    context = {
                "country": cnt
            }
    return render(request, 'country.html', context)
#    result = """
#    <h1>"Проект DjangoCountries"</h1>
#    <strong>Исполнитель</strong>: <i>Паницкий В.В.</i>
#    """
#    return HttpResponse(result)

def view_lang(request, id):
    try:
        lang = Language.objects.get(language=id)
        cnt = lang.country_set.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Языка с названием {id} не существует')
    context = {
                "lang": lang,
                "cnt": cnt
            }
    return render(request, 'lang.html', context)

def langs(request):
#    langs = []
#    with open('countries.json') as f:
#        cn = json.load(f)
#    for l1 in cn:
#        for l2 in l1['languages']:
#            if l2 not in langs:
#                langs.append(l2)
#    langs.sort()
    langs = Language.objects.all()
    context = {
        'lang': langs
    }
    return render(request, 'languages.html', context)


