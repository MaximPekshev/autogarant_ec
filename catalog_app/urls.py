from django.urls import path
from .views import show_catalog, show_good, show_search_result
from .views import show_category, show_manufacturer

urlpatterns = [
    path('category/<str:uid>/', show_category, name='show_category'),
    path('manufacturer/<str:uid>/', show_manufacturer, name='show_manufacturer'),
    path('search/', show_search_result, name='show_search_result'),
    path('<str:uid>/', show_good, name='show_good'),
    path('', show_catalog, name='show_catalog'),
]
