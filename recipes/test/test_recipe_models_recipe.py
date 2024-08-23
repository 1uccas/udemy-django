from django.core.exceptions import ValidationError
from parameterized import parameterized
from .test_recipes_base import TestRecipesBase

class RecipeModelTest(TestRecipesBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
    
    def test_recipe_title_raises_error_if_title_has_more_than_65_char(self):
        self.recipe.title = 'A' * 70
            
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()
    
    def test_recipe_fields_max_legth(self):
        # testar o maximo de caracteres dos itens do banco de dados
        filds = [
                ('title', 65),
                ('description', 165),
                ('preparation_time_unit', 65),
                ('servings_unit', 65),
            ]
        for fild, max_legth in filds:
            with self.subTest(fild=fild, max_legth=max_legth):
                # permite modificar ou adicionar atributos a objetos dinamicamente durante a execução do programa
                setattr(self.recipe, fild, 'A' * (max_legth + 0))
                    
                with self.assertRaises(ValidationError): #Try catch (chamada de exceção)
                    self.recipe.full_clean()
            
             
        