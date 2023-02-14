from django.shortcuts import render, HttpResponse

def home(request):
    result = """
    <h1>"Проект DjangoCountries"</h1>
    <strong>Исполнитель</strong>: <i>Паницкий В.В.</i>
    """
    return HttpResponse(result)
