from django.contrib import admin

# Register your models here.
from goods.models import Categories, Product

#admin.site.register(Categories)
#admin.site.register(Product)

@admin.register(Categories)
class admin_Categories(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}

@admin.register(Product)
class admin_Product(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}