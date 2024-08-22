from django.core.exceptions import ValidationError

from .test_recipes_base import TestRecipesBase

class RecipeModelTest(TestRecipesBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_char(self):
        self.recipe.title = 'A' * 70
        
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()