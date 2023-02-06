from django.db import models
from uuslug import slugify
from django.db.models import Sum

class Manufacturer(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default='')
    cpu_slug = models.SlugField(max_length=256, verbose_name='ЧПУ_Url', null=True, blank=True, default='')

    def __str__(self):
        return self.uid

    def save(self, *args, **kwargs):
        self.cpu_slug = '{}'.format(slugify(self.name))	
        super(Manufacturer, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Производитель'
        verbose_name_plural = 'Производители'

class Category(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    code = models.CharField(max_length=150, verbose_name='Код', null=True, blank=True, default='')
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default='')
    cpu_slug = models.SlugField(max_length=256, verbose_name='ЧПУ_Url', null=True, blank=True, default='')

    def __str__(self):
        return self.uid

    def save(self, *args, **kwargs):
        self.cpu_slug = '{}'.format(slugify(self.name))	
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
    

class Good(models.Model):
    
    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    code = models.CharField(max_length=100, verbose_name='Код', null=True, blank=True, default='')
    art = models.CharField(max_length=100, verbose_name='Артикул', null=True, blank=True, default='')
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default='')
    okei = models.CharField(max_length=100, verbose_name='Единица измерения', null=True, blank=True, default='')
    cpu_slug = models.SlugField(max_length=256, verbose_name='ЧПУ_Url', null=True, blank=True, default='')
    category = models.ForeignKey(Category, verbose_name='Категория', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)
    manufacturer = models.ForeignKey(Manufacturer, verbose_name='Производитель', on_delete=models.SET_DEFAULT,null=True, blank=True, default=None)

    def __str__(self):
        return '{}'.format(self.uid)

    def save(self, *args, **kwargs):
        self.cpu_slug = '{}'.format(slugify(self.name))	
        super(Good, self).save(*args, **kwargs)

    def get_price(self):
        try:
            price = Price.objects.filter(good=self, price_type__name='ОПТ БЕЗНАЛ').first().price
        except:
            price = 0
        return price

    def get_all_prices(self):
        prices = Price.objects.filter(good=self, price_type__name='ОПТ БЕЗНАЛ')
        return prices

    def get_all_stock_balances(self):
        stock_balances = StockBalance.objects.filter(good=self)
        return stock_balances    

    def get_stock_balance(self):
        stock_balance = StockBalance.objects.filter(good=self).aggregate(Sum('free')).get("free__sum")
        if stock_balance:
            return stock_balance
        else:
            return 0    

    def get_image(self):
        return Picture.objects.filter(good=self).first()        

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

def get_image_name(instance, filename):
	
	new_name = ('%s' + '.' + filename.split('.')[-1]) % instance.uid
	return new_name

class Picture(models.Model):
    
    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    title = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default=None)
    # image = models.ImageField(upload_to=get_image_name, verbose_name='Изображение', default=None)
    good = models.ForeignKey(Good, verbose_name='Товар', on_delete=models.CASCADE)
    src = models.CharField(max_length=256, verbose_name='Изображение', null=True, blank=True, default=None)
    
    def __str__(self):
        return '{}'.format(self.uid)

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

class PriceType(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    code = models.CharField(max_length=100, verbose_name='Код', null=True, blank=True, default='')
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default='')

    def __str__(self):
        return '{}'.format(self.uid)

    class Meta:
        verbose_name = 'Тип цен'
        verbose_name_plural = 'Типы цен'

class Price(models.Model):

    price = models.DecimalField(verbose_name = 'Цена', max_digits=15, decimal_places=2, default=0)
    good = models.ForeignKey(Good, verbose_name='Товар', on_delete=models.CASCADE)
    price_type = models.ForeignKey(PriceType, verbose_name='Тип цены', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('good', 'price_type',)
        verbose_name = 'Цена товара'
        verbose_name_plural = 'Цены товаров'

class Division(models.Model):

    uid = models.SlugField(max_length=36, verbose_name='Идентификатор', unique=True)
    code = models.CharField(max_length=100, verbose_name='Код', null=True, blank=True, default='')
    name = models.CharField(max_length=256, verbose_name='Наименование', null=True, blank=True, default='')
    short_name = models.CharField(max_length=5, verbose_name='Сокращенное наименование', null=True, blank=True, default='')

    def __str__(self):
        return '{}'.format(self.uid)

    class Meta:
        verbose_name = 'Склад'
        verbose_name_plural = 'Склады'

class StockBalance(models.Model):

    stock = models.SmallIntegerField(verbose_name = 'Остаток', null=True, blank=True, default=0)
    reserve = models.SmallIntegerField(verbose_name = 'Резерв', null=True, blank=True, default=0)
    free = models.SmallIntegerField(verbose_name = 'Свободный остаток', null=True, blank=True, default=0)
    good = models.ForeignKey(Good, verbose_name='Товар', on_delete=models.CASCADE)
    division = models.ForeignKey(Division, verbose_name='Склад', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('good', 'division',)
        verbose_name = 'Остаток товара'
        verbose_name_plural = 'Остатки товаров'