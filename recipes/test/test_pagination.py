from pdb import set_trace
from unittest import TestCase
from django.urls import reverse
from recipes.models import Recipe
from .test_recipes_base import TestRecipesBase
from utils.pagination import make_pagination

class PaginationTest(TestRecipesBase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=1
            )['pagination']
        
        self.assertEqual([1,2,3,4], pagination)
        
    def test_pagination_more_or_not(self):
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=2
            )['pagination']
        
        self.assertEqual([1,2,3,4], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=3
            )['pagination']
        
        self.assertEqual([2,3,4,5], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=4
            )['pagination']
        
        self.assertEqual([3,4,5,6], pagination)
    
    def test_make_sure_middle_ranges_are_correct(self):
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=12
            )['pagination']
        
        self.assertEqual([11,12,13,14], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=15
            )['pagination']
        
        self.assertEqual([14,15,16,17], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=18
            )['pagination']
        
        self.assertEqual([17,18,19,20], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=19
            )['pagination']
        
        self.assertEqual([17,18,19,20], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=20
            )['pagination']
        
        self.assertEqual([17,18,19,20], pagination)
        
    def test_whether_the_page_template_is_being_displayed_correctly(self):
        title = "Comida de gato"
        description = "lorem-lorem-lorem-lorem"
        
        self.make_recipe(
            title=title,
            description=description,
        )
        
        response = self.client.get(reverse('recipes:home'))
        
        #title
        self.assertIn((title).encode(), response.content)
        
        #description
        self.assertIn((description).encode(), response.content)
        
        self.assertEqual(len(response.context['recipes']), 1)
        self.assertEqual(len(response.context['pagination_range']), 9)
        set_trace()