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
        