from django.shortcuts import render, HttpResponse
from pathlib import Path
from django.views.decorators.csrf import csrf_exempt
import json
from catalog_app.models import Good, Category, Picture, Manufacturer
from catalog_app.models import Price, PriceType
from catalog_app.models import StockBalance, Division
from django.db.models import Q
from decouple import config
# from PIL import Image
# import io
# import base64
# import os
# from django.core.files import File
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

@csrf_exempt
def upload_goods_json(request):
    if request.method == "POST":
        api_key = request.headers.get('API-TOKEN')
        if api_key == config('INCOMING_API_KEY'):
            goods = json.loads(request.body.decode("utf-8-sig"))
            for good in goods.get("goods"):
                try:
                    good_obj = Good.objects.get(uid=good.get("uid"))
                except:
                    good_obj = Good(uid=good.get("uid"))
                good_obj.code = good.get("code")
                good_obj.art = good.get("art")
                good_obj.name = good.get("name")
                good_obj.okei = good.get("okei")
                category = good.get("category")
                manufacturer = good.get("manufacturer")
                if category:
                    try:
                        category_obj = Category.objects.get(uid=category.get("uid"))
                    except:
                        category_obj = Category(uid=category.get("uid"))
                    category_obj.code = category.get("code")
                    category_obj.name = category.get("name")
                    category_obj.save()
                    good_obj.category = category_obj
                if manufacturer:
                    try:
                        manufacturer_obj = Manufacturer.objects.get(uid=manufacturer.get("uid"))
                    except:
                        manufacturer_obj = Manufacturer(uid=manufacturer.get("uid"))
                    manufacturer_obj.name = manufacturer.get("name")
                    manufacturer_obj.save()
                    good_obj.manufacturer = manufacturer_obj
                good_obj.save()    
                picture = good.get("picture")
                if picture:
                    try:
                        picture_obj = Picture.objects.get(uid=picture.get("uid"))
                    except:
                        picture_obj = Picture(uid=picture.get("uid"))
                    picture_obj.title = good_obj.name
                    picture_obj.good = good_obj
                    base_path = 'https://sto-gs.ru/media/'
                    src = base_path  + picture.get("uid") + '.' + picture.get("extention")
                    picture_obj.src = src
                    picture_obj.save()

        else:
            return HttpResponse('Не корректный API-TOKEN')            
        return HttpResponse('Загрузка прошла успешно')

@csrf_exempt
def upload_prices_json(request):
    if request.method == "POST":
        api_key = request.headers.get('API-TOKEN')
        if api_key == config('INCOMING_API_KEY'):
            prices = json.loads(request.body.decode("utf-8"))
            for price in prices.get("prices"):
                price_type = price.get("kind")
                try:
                    price_obj = Price.objects.get(Q(good__uid=price.get("uid")) & Q(price_type__uid=price_type.get("uid")))
                except:
                    try:
                        price_type_obj = PriceType.objects.get(uid=price_type.get("uid"))
                    except:
                        price_type_obj = PriceType(uid=price_type.get("uid"))    
                    price_type_obj.code = price_type.get("code")
                    price_type_obj.name = price_type.get("name")
                    price_type_obj.save()
                    try:
                        good_obj = Good.objects.get(uid=price.get("uid"))
                    except:
                        continue
                    price_obj = Price(
                        good = good_obj,
                        price_type = price_type_obj
                    )
                price_obj.price = price.get("price")
                price_obj.save()
        else:
            return HttpResponse('Не корректный API-TOKEN')            
        return HttpResponse('Загрузка прошла успешно')

@csrf_exempt
def upload_quantities_json(request):
    if request.method == "POST":
        api_key = request.headers.get('API-TOKEN')
        if api_key == config('INCOMING_API_KEY'):
            quantities = json.loads(request.body.decode("utf-8"))
            for quantity in quantities.get("quantities"):
                division = quantity.get("division")
                try:
                    quantity_obj = StockBalance.objects.get(Q(good__uid=quantity.get("uid")) & Q(division__uid=division.get("uid")))
                except:
                    try:
                        division_obj = Division.objects.get(uid=division.get("uid"))
                    except:
                        division_obj = Division(uid=division.get("uid"))    
                    division_obj.code = division.get("code")
                    division_obj.name = division.get("name")
                    division_obj.save()
                    try:
                        good_obj = Good.objects.get(uid=quantity.get("uid"))
                    except:
                        continue
                    quantity_obj = StockBalance(
                        good = good_obj,
                        division = division_obj
                    )
                quantity_obj.stock = quantity.get("stock")
                quantity_obj.reserve = quantity.get("reserve")
                quantity_obj.free = quantity.get("free")
                quantity_obj.save()
        else:
            return HttpResponse('Не корректный API-TOKEN')            
        return HttpResponse('Загрузка прошла успешно')