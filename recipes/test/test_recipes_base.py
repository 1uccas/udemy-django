from django.test import TestCase
from recipes.models import Category, User, Recipe

class TestRecipesBase(TestCase):
    def setUp(self) -> None:
        category = Category.objects.create(name='category') # create a category
        author = User.objects.create_user( # Create a author
            first_name='first_name',
            last_name='last_name',
            username='username',
            password='123456',
            email='email@teste.com',
        )
        recipe = Recipe.objects.create( #Create a Recipe
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