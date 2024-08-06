from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from recipes.views import contato, home, sobre

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('sobre/', sobre),
    path('contato/', contato)
]