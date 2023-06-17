from django.db import models
from django.template.defaultfilters import slugify
from django.core.exceptions import ValidationError

# Create your models here.

class Category(models.Model):

    title = models.CharField(max_length=30, unique=True, verbose_name='Hазваниe')
    slug = models.SlugField()

    def save(self, *args, **kwargs):
        if self.parent and self.parent.name == self.name:
            raise ValidationError('Xato...')
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Store(models.Model):

    title = models.CharField(max_length=255)
    slug = models.SlugField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    location = models.CharField(max_length=255)

    def save(self, *args, **kwargs):
        if self.parent and self.parent.name == self.name:
            raise ValidationError('Xato...')
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class Product(models.Model):

    title = models.CharField(max_length=150, unique=True, verbose_name='Заголовок статьи')
    slug = models.SlugField()
    content = models.TextField(verbose_name='Содержание статьи')
    photo = models.ImageField(upload_to='photos/', verbose_name='Фотография',
                              null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_date = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    publish = models.BooleanField(default=True, verbose_name='Статус статьи')
    views = models.IntegerField(default=0, verbose_name='Количество просмотров')
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')
    

    def save(self, *args, **kwargs):
        if self.parent and self.parent.name == self.name:
            raise ValidationError('Xato...')
        else:
            if not self.slug:
                self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Image(models.Model):

    image = models.ImageField(upload_to='static/image')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    
