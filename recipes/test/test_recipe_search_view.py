from django.urls import reverse, resolve
from .test_recipes_base import TestRecipesBase
from recipes.models import Category, User, Recipe
import unittest # skip and fail

import pdb # import debugger

from recipes import views

class RecipeSearchViewTest(TestRecipesBase):
    def test_recipe_search_uses_correct_view_function(self):
        resolved = resolve(reverse('recipes:search'))
        self.assertIs(resolved.func, views.search)
        
    def test_recipes_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=test')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')
        
    def test_recipe_search_raises_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)
        
    def test_search_caracter_escape(self):
        response = self.client.get(reverse('recipes:search') + '?q=<script><h1>Test</h1></script>')
        self.assertIn(("&quot;&lt;script&gt;&lt;h1&gt;Test&lt;/h1&gt;&lt;/script&gt;&quot;").encode('utf-8'), response.content)
        
    def test_recipe_search_can_find_recipe_by_title(self):
        TermSearchNoFind = 'This test will not found'
        DescriptionSearchNoFind = 'Description not found'
        
        TermSearchFind = 'This test will found'
        DescriptionSearchFind = 'Desciprtion found'
        
        self.make_recipe(
            title=TermSearchFind,
            description=DescriptionSearchFind,
        )
        
        url = reverse('recipes:search')
        responseFind = self.client.get(url + f'?q={TermSearchFind}')
        self.assertIn(DescriptionSearchFind.encode('utf-8'), responseFind.content)
        self.assertIn(TermSearchFind.encode('utf-8'), responseFind.content)
        
        self.assertNotIn(TermSearchNoFind.encode('utf-8'), responseFind.content)
        self.assertNotIn(DescriptionSearchNoFind.encode('utf-8'), responseFind.content)
        
        
        
        