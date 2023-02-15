from django.shortcuts import render, HttpResponse
from django.http import HttpResponseNotFound
import json

def home(request):
    context = {
        "pr_name": 'Проект DjangoCountries',
        "creator": "Паницкий В.В."
    }
    return render(request, 'index.html', context)


def countries_list(request):
    with open('countries.json') as f:
        cn = json.load(f)
    context = {
        "cnts": cn
    }
    return render(request, 'countries-list.html', context)

def view_country(request, id):
    with open('countries.json') as f:
        cn = json.load(f)
    for c in cn:
        if c['country'] == id:
            context = {
                "name": c['country'],
                "lang": c['languages']
            }
    return render(request, 'country.html', context)
#    result = """
#    <h1>"Проект DjangoCountries"</h1>
#    <strong>Исполнитель</strong>: <i>Паницкий В.В.</i>
#    """
#    return HttpResponse(result)

def langs(request):
    langs = []
    with open('countries.json') as f:
        cn = json.load(f)
    for l1 in cn:
        for l2 in l1['languages']:
            if l2 not in langs:
                langs.append(l2)
    langs.sort()
    context = {
        'lang': langs
    }
    return render(request, 'languages.html', context)


