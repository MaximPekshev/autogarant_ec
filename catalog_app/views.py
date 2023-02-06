from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from rest_framework import generics, permissions
from django.core.paginator import Paginator
import datetime
from .models import Manufacturer
from .models import Category
from .serializers import CategorySerializer
from .models import Good
from .serializers import GoodSerializer
from .models import Price
from django.db.models import Q

class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uid'

class GoodList(generics.ListCreateAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class GoodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Good.objects.all()
    serializer_class = GoodSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    lookup_field = 'uid'

def get_highest_price(goods):
    highest_price = Price.objects.filter(price__gte=0,good__in=goods, price_type__name='Розничные').order_by('-price').first()
    if highest_price:
        return highest_price.price
    else:
        return None    
def get_lowest_price(goods):
    lowest_price = Price.objects.filter(price__gte=0,good__in=goods, price_type__name='Розничные').order_by('price').first()
    if lowest_price:
        return lowest_price.price
    else:
        return None

def show_catalog(request):
    goods = Good.objects.all()
    
    # min_price = request.GET.get('min_price')
    # max_price = request.GET.get('max_price')

    goods_count=56
    page_number = request.GET.get('page', 1)
    paginator = Paginator(goods, goods_count)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''	
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''
    context = {
		'page_object': page,
        'prev_url': prev_url,
        'next_url': next_url,
        'is_paginated': is_paginated,
        # 'highest_price': get_highest_price(goods),
        # 'lowest_price': get_lowest_price(goods),
        'actual_year': datetime.datetime.now().strftime("%Y"),
        'categories': Category.objects.all(),
	}
    return render(request, 'catalog_app/catalog.html', context)

def show_good(request, uid):
    good = get_object_or_404(Good, uid=uid)
    context = {
        'good': good,
        'actual_year': datetime.datetime.now().strftime("%Y"),
    }

    return render(request, 'catalog_app/good.html', context)

def show_search_result(request):

    if request.method == 'GET':
        query = request.GET.get('q')
        goods = Good.objects.filter(
			Q(name__icontains=query) |
			Q(art__icontains=query)
		)
        if len(goods) == 1:
            return redirect('show_good', uid=goods[0].uid)
        goods_count=18
        page_number = request.GET.get('page', 1)
        paginator = Paginator(goods, goods_count)
        page = paginator.get_page(page_number)
        is_paginated = page.has_other_pages()
        if page.has_previous():
            prev_url = '?q={}&page={}'.format(query ,page.previous_page_number())
        else:
            prev_url = ''	
        if page.has_next():
            next_url = '?q={}&page={}'.format(query, page.next_page_number())
        else:
            next_url = ''
        context = {
            'page_object': page,
            'prev_url': prev_url,
            'next_url': next_url,
            'is_paginated': is_paginated,
            # 'highest_price': get_highest_price(goods),
            # 'lowest_price': get_lowest_price(goods),
            'actual_year': datetime.datetime.now().strftime("%Y"),
            'search_query': query,
        }
        return render(request, 'catalog_app/search.html', context)

def show_category(request, uid):
    category = get_object_or_404(Category, uid=uid)
    goods = Good.objects.filter(category=category)
    goods_count=56
    page_number = request.GET.get('page', 1)
    paginator = Paginator(goods, goods_count)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''	
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'prev_url': prev_url,
        'next_url': next_url,
        'is_paginated': is_paginated,
        'category': category,
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'actual_year': datetime.datetime.now().strftime("%Y"),
    }
    return render(request, 'catalog_app/category.html', context)

def show_manufacturer(request, uid):
    manufacturer = get_object_or_404(Manufacturer, uid=uid)
    goods = Good.objects.filter(manufacturer=manufacturer)
    goods_count=56
    page_number = request.GET.get('page', 1)
    paginator = Paginator(goods, goods_count)
    page = paginator.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''	
    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {
        'page_object': page,
        'prev_url': prev_url,
        'next_url': next_url,
        'is_paginated': is_paginated,
        'manufacturer': manufacturer,
        'categories': Category.objects.all(),
        'manufacturers': Manufacturer.objects.all(),
        'actual_year': datetime.datetime.now().strftime("%Y"),
    }
    return render(request, 'catalog_app/manufacturer.html', context)