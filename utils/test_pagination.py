from unittest import TestCase

from utils.pagination import make_pagination

class PaginationTest(TestCase):
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
        