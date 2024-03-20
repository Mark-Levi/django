<<<<<<< HEAD
from django.http import HttpResponse
=======
from django.http import HttpResponse, HttpResponseNotFound
>>>>>>> 17e3ff9466109769989c1a8cf0e70b7d4c7a46bd
from django.shortcuts import render


# Create your views here.
def index(request):
<<<<<<< HEAD
    return HttpResponse("Страница приложения MYSITE")


def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")
=======
    return HttpResponse("Страница моего сайта")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"<h1>Страница категорий</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
>>>>>>> 17e3ff9466109769989c1a8cf0e70b7d4c7a46bd
