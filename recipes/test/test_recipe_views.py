from django.test import TestCase
from django.urls import reverse, resolve
from recipes.models import Category, User, Recipe

import pdb # import debugger

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
        
    '''Create category, recipe and author; insert data in database and test yours templates '''    
    def test_recipe_home_template_loads_recipes(self): # Criar uma categoria e testar o template
        category = Category.objects.create(name='category') # Criei uma categoria
        author = User.objects.create_user( # Criei um author
            first_name='first_name',
            last_name='last_name',
            username='username',
            password='123456',
            email='email@teste.com',
        )
        recipe = Recipe.objects.create( #Criei um Recipe
            category=category,
            author=author,
            title = 'Recipe Title',
            description = 'Recipe Description',
            slug = 'Recipe-slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 10,
            servings_unit = 'Pessoas',
            preparation_steps = 'Recipes Preparation Steps',
            preparation_steps_is_html = False,
            is_published = True,
        )
        #pdb.set_trace() # 'breakpoint()' will be stopped here
        ...
        response = self.client.get(reverse('recipes:home'))
        self.assertIn(('Recipe Title').encode('utf-8'), response.content)
        self.assertIn(('Recipe Description').encode('utf-8'), response.content)
        
        self.assertEqual(len(response.context['recipes']), 1)
        '''
        analyze whether the creation of objects was successful
        We return the number of items from response.context['recipes']
        If response.context == 0 -> Fail (no collection of objects is being passed to the context);
        Else -> Pass (there is a collection of objects being passed to the context)
        '''
        
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
        