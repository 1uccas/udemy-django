from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.core.paginator import Paginator
from django.db.models import Q
from recipes.models import Recipe
from django.http import Http404
from utils.pagination import make_pagination
from utils.pagination import pagination

def home(request):
    recipes = Recipe.objects.filter(
            is_published=True,
        ).order_by('-id')
    
    page_obj, pagination_range = pagination(request, recipes, 9)
    
    return render(request, "recipes/pages/home.html", context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
    })
    
def category(request, category_id):
    '''recipes = Recipe.objects.filter(
        category__id=category_id, is_published=True
        ).order_by('-id')
    
    if not recipes:
        raise Http404('Not Found 404')'''
        
        
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category__id=category_id, is_published=True
        ).order_by('-id')
    )
    
    page_obj, pagination_range = pagination(request, recipes, 9)
    
    return render(request, "recipes/pages/category.html", context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category'
    })
    
def recipe(request, id):
    """recipe = Recipe.objects.filter(
        id=id, is_published=True
        ).order_by('-id').first()"""
    
    recipe = get_object_or_404(Recipe, id=id, is_published=True)
    
    return render(request, "recipes/pages/recipe-view.html", context={
        'recipe': recipe,
        'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q', '').strip()
    
    if not search_term:
        raise Http404()
    
    recipe = Recipe.objects.filter(
        Q(
            Q(title__contains=search_term)|
            Q(description__contains=search_term)
        ),
        is_published=True).order_by('-id')
    
        #(i)contains para ignorar letras maiusculas e minusculas na busca
    
    page_obj, pagination_range = pagination(request, recipe, 9)
    
    return render(request, "recipes/pages/search.html", context={
        'page_title': f'Search to "{search_term}" in',
        'search_found': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })