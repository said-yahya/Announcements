from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=30, unique=True, verbose_name='Hазваниe')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

class Product(models.Model):
    title = models.CharField(max_length=150, unique=True, verbose_name='Заголовок статьи')
    content = models.TextField(verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография',
                              null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    publish = models.BooleanField(default=True, verbose_name='Статус статьи')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

