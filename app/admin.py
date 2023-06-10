from django.contrib import admin

# Register your models here.
from app.models import *

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display=['id', 'title', 'discount_price', 'selling_price','category','product_image']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display=['id','user','locality','city','state','zipcode']
    
    
@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display=['id','user','product','quantity']

