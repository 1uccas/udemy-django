
from django.urls import path
from recipes.views import home
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"), #<id> para receber o id na url | <int:> para receber apenas numero int
]