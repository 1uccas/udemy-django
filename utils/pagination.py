import math
from django.core.paginator import Paginator
from pdb import set_trace

# python -c
# "import string as s;from random import SystemRandom as
# sr;print(''.join(sr().choices(s.ascii_letters +
# s.punctuation, k=64)))"

def make_pagination(
    page_range, # interseção de páginas
    qtd_page, # limite por páginas
    current_page, # página atual
):

    middle = math.ceil(qtd_page / 2)
    start = current_page - middle
    end = current_page + middle
    total_pages = len(page_range)
    
    # caso o start coloque como positivo caso ele for menor que zero (negativo) ou caso não for
    negative_start = abs(start) if start < 0 else 0

    # caso o retorno do start se torne negativo, torne o start como zero e incremente ao negative_start:
    # end = end + negative_start
   
    if start < 0:
        start = 0
        end += negative_start
    
    # se o end for maior ou igual ao total de páginas, realize o seguinte calculo com o start:
    # start recebe start menos (caso for negativo, deixe-o positivo) o calculo de: end menos o total de páginas
    # isso para a interseção se tornar estatica quando o end for maior que o total de páginas
    
    if end >= total_pages:
        start = start - abs(end - total_pages)   
    
    pagination = page_range[start:end]
    
    return {
        'pagination': pagination,
        'page_range': page_range,
        'qtd_page': qtd_page,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start,
        'end_range': end,
        'first_page_out_of_range': current_page > middle,
        'last_page_out_of_range': end < total_pages,
    }
    
def pagination(request, queryset, per_page, qtd_page=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1
    
    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)
    
    pagination_range = make_pagination(
        paginator.page_range,
        qtd_page,
        current_page
    )
    
    return page_obj, pagination_range