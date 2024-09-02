import math

def make_pagination(
    page_range, # interseção de páginas
    qtd_page, # limite por páginas
    current_page, # página atual
):

    middle = math.ceil(qtd_page / 2)
    start = current_page - middle
    end = current_page + middle
    
    negative_start = abs(start) if start < 0 else 0

    # caso o retorno do start se torne negativo
    if start < 0:
        start = 0
        end += negative_start
        
    return page_range[start:end]