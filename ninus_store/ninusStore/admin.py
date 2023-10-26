from django.contrib import admin
from .models import Collection,Order,Product,Wishlist,Purchase


class ProductInline(admin.StackedInline):
    model=Product
    extra=0


class PurchaseInline(admin.StackedInline):
    model=Purchase
    extra=0


class CollectionAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class WishlistAdmin(admin.ModelAdmin):
    inlines = [ProductInline]


class OrderAdmin(admin.ModelAdmin):
    inlines = [PurchaseInline]


# Register your models here.
admin.site.register(Collection,CollectionAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(Product)
admin.site.register(Wishlist,WishlistAdmin)
admin.site.register(Purchase)
