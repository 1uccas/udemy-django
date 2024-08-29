from django.urls import reverse, resolve
from .test_recipes_base import TestRecipesBase
from recipes.models import Category, User, Recipe
import unittest # skip and fail

import pdb # import debugger

from recipes import views

class RecipeCategoryViewTest(TestRecipesBase):
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
        
    def test_recipe_category_template_loads_recipes(self):
        varTitle = "This is my category"
        self.make_recipe(title=varTitle)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIn((varTitle).encode('utf-8'), response.content)
    
    def test_recipe_category_template_is_published_False(self):
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        
        self.assertIn(('<h1>Not Found</h1>').encode('utf-8'), response.content)
        
    def test_category_404_when_it_does_not_exist(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 999}))
        self.assertEqual(response.status_code, 404)

