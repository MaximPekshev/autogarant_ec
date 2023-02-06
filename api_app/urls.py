from django.urls import path
from catalog_app.views import CategoryList, CategoryDetail
from catalog_app.views import GoodList, GoodDetail
from .views import upload_goods_json, upload_prices_json, upload_quantities_json

urlpatterns = [
    path('category/list/', CategoryList.as_view()),
    path('category/<str:uid>/', CategoryDetail.as_view()),
    path('good/list/', GoodList.as_view()),
    path('good/<str:uid>/', GoodDetail.as_view()),
    path('upload/goods/', upload_goods_json),
    path('upload/prices/', upload_prices_json),
    path('upload/quantities/', upload_quantities_json),
]    