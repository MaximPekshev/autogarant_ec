from rest_framework import serializers
from .models import Category, Good, Picture, Manufacturer

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = (
            'cpu_slug', 'id',
        )

class GoodSerializer(serializers.ModelSerializer):
    category_uid = serializers.CharField(source='category.uid', label='Категория', required=False)
    manufacturer_uid = serializers.CharField(source='manufacturer.uid', label='Производитель', required=False)
    class Meta:
        model = Good
        fields = (
            'uid',
            'code',
            'art',
            'name',
            'okei',
            'category_uid',
            'manufacturer_uid'

        )

    def create(self, validated_data):
        try:
            category_uid = validated_data.pop('category')
        except:
            category_uid = None
        try:
            manufacturer_uid = validated_data.pop('manufacturer')
        except:
            manufacturer_uid = None    
        instance = Good.objects.create(**validated_data)
        try:
            category = Category.objects.get(uid=category_uid.get('uid'))
        except:
            category = None
        try:
            manufacturer = Manufacturer.objects.get(uid=manufacturer_uid.get('uid'))
        except:
            manufacturer = None    
        instance.category = category
        instance.manufacturer = manufacturer
        instance.save()
        return instance
    def update(self, instance, validated_data):
        try:
            category_uid = validated_data.pop('category')
        except:
            category_uid = None
        try:
            manufacturer_uid = validated_data.pop('manufacturer')
        except:
            manufacturer_uid = None    
        instance = super().update(instance, validated_data)
        try:
            category = Category.objects.get(uid=category_uid.get('uid'))
        except:
            category = None
        try:
            manufacturer = Manufacturer.objects.get(uid=manufacturer_uid.get('uid'))
        except:
            manufacturer = None    
        instance.category = category
        instance.manufacturer = manufacturer
        instance.save()
        return instance

class PictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Picture
        fields = ('__all__')