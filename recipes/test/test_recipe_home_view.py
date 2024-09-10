from django.urls import reverse, resolve
from .test_recipes_base import TestRecipesBase
from recipes.models import Category, User, Recipe
from unittest.mock import patch
import unittest # skip and fail

import pdb # import debugger

from recipes import views

class RecipeHomeViewTest(TestRecipesBase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
    
    def test_recipe_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(('Recipe Title').encode('utf-8'), response.content)
        self.assertIn(('description').encode('utf-8'), response.content)
        
        self.assertEqual(len(response.context['recipes']), 1)
        '''
        analyze whether the creation of objects was successful
        We return the number of items from response.context['recipes']
        If response.context == 0 -> Fail (no collection of objects is being passed to the context);
        Else -> Pass (there is a collection of objects being passed to the context)
        '''
        
    def test_recipe_home_template_is_published_False(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(('<h1>No recipes found here 🥲</h1>').encode('utf-8'), response.content)
        
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200) # -> assertEqual(onde procurar, o que deseja achar)
    
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
        
    def test_recipe_home_is_paginated(self):
        for i in range(8):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)
            
        with patch("recipes.views.PER_PAGE", new=3):
            response = self.client.get(reverse('recipes:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator
            
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 2)