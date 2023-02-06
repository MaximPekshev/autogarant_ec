from django.contrib import admin
from .models import Category, Good, Picture, Price, PriceType, StockBalance, Division, Manufacturer

admin.site.register(Category)
admin.site.register(Good)
admin.site.register(Picture)
admin.site.register(Price)
admin.site.register(PriceType)
admin.site.register(StockBalance)
admin.site.register(Division)
admin.site.register(Manufacturer)