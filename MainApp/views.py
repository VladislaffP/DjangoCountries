from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json
from MainApp.models import Country
from MainApp.models import Language
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    context = {
        "pr_name": 'Проект DjangoCountries',
        "creator": "Паницкий В.В."
    }
    return render(request, 'index.html', context)


def countries_list(request):
#    with open('countries.json') as f:
#        cn = json.load(f)
    cn = Country.objects.all()
    context = {
        "cnts": cn
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


