from django.contrib import admin
from .models import *

# Register your models here.
### for log-in into the administration panel 'username: admin', 'password: 123' ###

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'views', 'content', 'created_date', 'updated_date', 'publish')
    list_display_links = ('title', )
    list_editable = ('publish', )
    readonly_fields = ('views', )
    exclude = ['slug']

class CategoryAdmin(admin.ModelAdmin):
    exclude = ['slug']

class StoreAdmin(admin.ModelAdmin):
    exclude = ['slug']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Image)
