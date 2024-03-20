from django.urls import path
from .views import index, categories

urlpatterns = [
    path("", index, name="main"),
    path("cats/<int:catid>/", categories),
]
