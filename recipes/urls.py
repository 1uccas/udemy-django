
from django.urls import path
from recipes.views import home
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/search/', views.search, name="search"),
    path('recipes/category/<int:category_id>/', views.category, name="category"), #<id> para receber o id na url | <int:> para receber apenas numero int
    path('recipes/<int:id>/', views.recipe, name="recipe"), #<id> para receber o id na url | <int:> para receber apenas numero int
]