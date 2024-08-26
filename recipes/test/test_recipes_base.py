from django.test import TestCase
from recipes.models import Category, User, Recipe

class TestRecipesBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    
    def make_recipe_preparation_steps_is_html_is_false_default(self):
        recipe = Recipe(
            category=self.make_category(name="Category Enter"),
            author=self.make_author(username="Jairzinho Rodrigues"),
            title='Recipe Title',
            description='description',
            slug='slug',
            preparation_time = 10,
            preparation_time_unit = 'Minutos',
            servings = 10,
            servings_unit = 'Pessoas',
            preparation_steps = 'Recipes Preparation Steps',
        )
        return recipe
    
    def make_author(
        self, 
        first_name='first_name',
        last_name='last_name',
        username='username',
        password="123456",
        email='author@email.com'):
        
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email,
        )
        
    def make_recipe(
        self,
        category=None,
        author=None,
        title='Recipe Title',
        description='description',
        slug='slug',
        preparation_time = 10,
        preparation_time_unit = 'Minutos',
        servings = 10,
        servings_unit = 'Pessoas',
        preparation_steps = 'Recipes Preparation Steps',
        preparation_steps_is_html = False,
        is_published = True
    ):
        
        '''if var_category ==  None:
            var_category = {}
        
        if var_author == None:
            var_author = {}'''
        
        return Recipe.objects.create(
            category=self.make_category(),
            author=self.make_author(),
            title = title,
            description = description,
            slug = slug,
            preparation_time = preparation_time,
            preparation_time_unit = preparation_time_unit,
            servings = servings,
            servings_unit = servings_unit,
            preparation_steps = preparation_steps,
            preparation_steps_is_html = preparation_steps_is_html,
            is_published = is_published,
        )
        