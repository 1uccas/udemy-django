from django.urls import reverse, resolve
from .test_recipes_base import TestRecipesBase
from recipes.models import Category, User, Recipe
import unittest # skip and fail

import pdb # import debugger

from recipes import views

class RecipeRecipeViewTest(TestRecipesBase):
    def test_recipe_recipes_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
    
    def test_recipe_recipe_template_is_published_False(self):
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        
        self.assertIn(('<h1>Not Found</h1>').encode('utf-8'), response.content)
        
    def test_recipe_recipe_template_loads_recipes(self):
        varTitle = "This is my title in recipe page"
        self.make_recipe(title=varTitle)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIn((varTitle).encode('utf-8'), response.content)
        
    def test_recipe_not_found_no_receipes_template(self):
        response = self.client.get(reverse('recipes:home')) #peguei o conteudo da página home
        self.assertIn(("<h1>No recipes found here 🥲</h1>").encode("utf-8"), response.content, "Error: HTML found")
        
        ''' 
        Looking for my HTML Tag within the response content 
        (for each string placed, it is necessary to encode to 'utf-8' to be transformed into n byte)
        ! Or vice versa (response.content.decode(utf-8) -> byte to String)

        '''
        
    def test_recipe_404_when_it_does_not_exist(self):  
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 999}))
        self.assertEqual(response.status_code, 404)