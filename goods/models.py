from dataclasses import Field
from email.mime import image
from django.db import models

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=150, unique=1, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=1, blank=1,null=1, verbose_name='добавочный url')

    class Meta:
        db_table = 'category'
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    def __str__(self) -> str:
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=150, unique=1, verbose_name='название')
    slug = models.SlugField(max_length=200, unique=1, blank=1,null=1, verbose_name='добавочный url')
    description = models.TextField(blank=1, null=1, verbose_name='описание')
    image = models.ImageField(upload_to='goods_imgs', blank=1, null=1)
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='цена')
    discount = models.DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='скидка')
    quantity =  models.PositiveIntegerField(default=0, verbose_name='кол-во')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = 'product'
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
    
    def __str__(self) -> str:
        return f'{self.name} - {self.quantity}'
    
    def display_id(self):
        return f'{self.id:05}'
    
    def total_price(self):
        if self.discount :
            return round(self.price*(100-self.discount)/100, 2)
        else:
            return self.price