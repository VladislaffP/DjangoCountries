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
    letters = string.ascii_uppercase
    request_full = request.GET
    start_letter = request_full.get("start_letter");
    filtered_countries = Country.objects.all().order_by("country")

    letter_param = ''

    if start_letter:
    #    print(lt)
        filtered_countries = filtered_countries.filter(country__startswith=start_letter)
        letter_param = 'start_letter=' + start_letter + '&'

    #print(rq.get("start_letter"))
    paginator = Paginator(filtered_countries, 10)
    #print(paginator.object_list)
    page_number = request_full.get('page')
    if not page_number:
        page_number = 1
    page_obj = paginator.get_page(page_number)
    page_content = page_obj.object_list

    nums_list = list(range(1, paginator.num_pages+1))
    start_num = (int(page_number) - 1) * 10 + 1;
    context = {
        #"cnts": cn,
        "letters": letters,
        'page_content': page_content,
        'total_pages': paginator.num_pages,
        'current_page': page_obj.number,
        'nums_list': nums_list,
        'letter_param': letter_param,
        'start_num': start_num
    }
    return render(request, 'countries-list.html', context)

def view_country(request, country_name):
    try:
        current_country = Country.objects.get(country=country_name)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Страны с названием {country_name} не существует')

#    with open('countries.json') as f:
#        cn = json.load(f)
#    for c in cn:
#        if c['country'] == id:
    context = {
                "country": current_country
            }
    return render(request, 'country.html', context)

def view_lang(request, language_name):
    try:
        current_language = Language.objects.get(language=language_name)
        language_countries_list = current_language.country_set.all()
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Языка с названием {language_name} не существует')
    context = {
                "current_language": current_language,
                "language_countries_list": language_countries_list
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
    languages_list = Language.objects.all()
    context = {
        'languages_list': languages_list
    }
    return render(request, 'languages.html', context)


