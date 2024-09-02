from unittest import TestCase

from utils.pagination import make_pagination

class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=1
            )
        
        self.assertEqual([1,2,3,4], pagination)
        
    def test_pagination_more_or_not(self):
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=2
            )
        
        self.assertEqual([1,2,3,4], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=3
            )
        
        self.assertEqual([2,3,4,5], pagination)
        
        pagination=make_pagination(
            page_range=list(range(1,21)),
            qtd_page=4,
            current_page=4
            )
        
        self.assertEqual([3,4,5,6], pagination)