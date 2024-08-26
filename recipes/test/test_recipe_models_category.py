from django.core.exceptions import ValidationError
from .test_recipes_base import TestRecipesBase

class CategoryModelTest(TestRecipesBase):
    def setUp(self) -> None:
        self.category = self.make_category()
        return super().setUp()
        
    def test_category_fields_max_lenght(self):
        setattr(self.category, 'name', 'A' * (66))
        with self.assertRaises(ValidationError):
            self.category.full_clean()
            
    def test_category_string_represetation(self):
        name = "This is just one test in Category"
        self.category.name = name
        self.category.full_clean()
        self.category.save()
        self.assertEqual(str(self.category.name), name, msg=f"<Error?> {self.category.name} != {name}")
        