from django.contrib import admin
from .models import *

# Register your models here.
### for log-in into the administration panel 'username: admin', 'password: 123' ###

class ProductAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'category', 'views', 'content', 'created_at', 'updated_at', 'publish')
    list_display_links = ('title', )
    list_editable = ('publish', )
    readonly_fields = ('views', )

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)

