from django.db import models
from django.conf import settings

# Create your models here.
NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание')
    preview = models.ImageField(upload_to='product/', verbose_name='превью', **NULLABLE)
    category = models.ForeignKey('catalog.Category', on_delete=models.PROTECT, verbose_name='категория', **NULLABLE)
    price = models.PositiveIntegerField(verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания', **NULLABLE)
    last_modified_date = models.DateTimeField(auto_now_add=True, verbose_name='последнее изменение', **NULLABLE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, **NULLABLE, verbose_name='пользователь')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='наименование')
    description = models.TextField(verbose_name='описание', **NULLABLE)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='продукт')
    number = models.FloatField(verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    is_active = models.BooleanField(default=False, verbose_name='активная')

    def __str__(self):
        return f'{self.name}({self.number})'

    class Meta:
        verbose_name = 'версия'
        verbose_name_plural = 'версии'
