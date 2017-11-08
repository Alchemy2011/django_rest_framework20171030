from django.contrib import admin

# Register your models here.
from computerapp.models import UserProfile, Category, Manufacturer, Product, DeliveryAddress, Order


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Category, CategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


admin.site.register(Manufacturer, ManufacturerAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'model', 'price', 'category', 'manufacturer', 'sold', ]
    list_editable = ['price', 'sold', 'category', ]


admin.site.register(Product, ProductAdmin)


class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'contact_person', 'contact_mobile_phone', 'delivery_address', ]


admin.site.register(DeliveryAddress, DeliveryAddressAdmin)


class UserProfileAdmin(admin.ModelAdmin):
    # 把关键字段显示出来，省一次点击
    list_display = ['id', 'mobile_phone', 'nickname', 'user', ]


admin.site.register(UserProfile, UserProfileAdmin)


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user', ]


admin.site.register(Order, OrderAdmin)
