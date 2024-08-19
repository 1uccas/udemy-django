from django.test import TestCase
from django.urls import reverse, resolve

from recipes import views

class RecipeViewsTest(TestCase):
    def test_recipe_home_view_function_is_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertIs(view.func, views.home)
        
    def test_recipe_category_view_function_is_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)
    
    def test_recipe_recipes_view_function_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)
    
        
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
        