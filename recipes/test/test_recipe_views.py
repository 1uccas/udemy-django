from django.urls import reverse, resolve
from .test_recipes_base import TestRecipesBase
from recipes.models import Category, User, Recipe
import unittest # skip and fail

import pdb # import debugger

from recipes import views

class RecipeViewsTest(TestRecipesBase):    
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_recipes_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
           
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
        
    def test_recipe_category_template_is_published_False(self):
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        
        self.assertIn(('<h1>Not Found</h1>').encode('utf-8'), response.content)
    
    def test_recipe_recipe_template_is_published_False(self):
        self.make_recipe(is_published=False)
        
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        
        self.assertIn(('<h1>Not Found</h1>').encode('utf-8'), response.content)
        
    def test_recipe_category_template_loads_recipes(self):
        varTitle = "This is my category"
        self.make_recipe(title=varTitle)
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIn((varTitle).encode('utf-8'), response.content)
        
    def test_recipe_recipe_template_loads_recipes(self):
        varTitle = "This is my title in recipe page"
        self.make_recipe(title=varTitle)
        response = self.client.get(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIn((varTitle).encode('utf-8'), response.content)
        
    def test_recipe_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertEqual(response.status_code, 200) # -> assertEqual(onde procurar, o que deseja achar)
    
    def test_recipe_home_view_loads_correct_template(self):
        response = self.client.get(reverse('recipes:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')
    
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
    
    def test_category_404_when_it_does_not_exist(self):
        response = self.client.get(reverse('recipes:category', kwargs={'category_id': 999}))
        self.assertEqual(response.status_code, 404)
    
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

        