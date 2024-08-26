from django.core.exceptions import ValidationError
from parameterized import parameterized
from .test_recipes_base import TestRecipesBase

class RecipeModelTest(TestRecipesBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        self.recipe = self.make_recipe()
        return super().setUp()
    
    @parameterized.expand([
        ('title', 65),
        ('description', 165),
        ('preparation_time_unit', 65),
        ('servings_unit', 65),
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        
    def test_recipe_preparation_steps_is_html_not_default(self):
        recipe = self.make_recipe_preparation_steps_is_html_is_false_default()
        recipe.full_clean()
        self.assertFalse(recipe.preparation_steps_is_html)
        
    def test_recipe_is_published_is_not_default(self):
        recipe = self.make_recipe_preparation_steps_is_html_is_false_default()
        recipe.full_clean()
        self.assertFalse(recipe.is_published)
        
    def test_category_fields_max_lenght(self):
        setattr(self.category, 'name', 'A' * (66))
        with self.assertRaises(ValidationError):
            self.category.full_clean()
            
    def test_recipe_string_represetation(self):
        title = "This is just one test"
        self.recipe.title = title
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe.title), title, msg=f"<Error?> {self.recipe.title} != {title}")
        