from django.contrib import admin

# Register your models here.
# https://docs.djangoproject.com/en/1.11/ref/contrib/admin/
from computerapp.models import Product, Category, Manufacturer, DeliveryAddress, UserProfile, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
admin.site.register(Category, CategoryAdmin)


class ManufactureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
admin.site.register(Manufacturer, ManufactureAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'price', 'category', 'manufacturer', 'sold', )
    list_editable = ('price', 'sold', 'category', )
admin.site.register(Product, ProductAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address')
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'mobile_phone', 'nickname')
admin.site.register(UserProfile, UserProfileAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'status')
admin.site.register(Order, OrderAdmin)
