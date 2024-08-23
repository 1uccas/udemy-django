from django.core.exceptions import ValidationError
from parameterized import parameterized
from .test_recipes_base import TestRecipesBase

class RecipeModelTest(TestRecipesBase):
    def setUp(self) -> None:
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
        breakpoint()
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
        
        