from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница моего сайта")


def categories(request, catid):
    if request.GET:
        print(request.GET)
    return redirect("main", permanent=True)
    # return HttpResponse(f"<h1>Страница категорий</h1><p>{catid}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")
