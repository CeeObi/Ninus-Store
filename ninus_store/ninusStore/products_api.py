from django.contrib.auth.models import User

from .models import Product, Wishlist, Purchase, Collection, Order, Cart, UserCart
from .data import data, cart_items



data_index = []
for index in range(0, len(data)):
    indx = index + 1
    data_index.append({"id":indx, "img_url":data[index],"prod_name":"white tee", "collection":{"col_name":"Jackets and tops"},"price":"199.9"})



class StoreData():
    def __init__(self):
        self.products=Product.objects.all()
        self.product=Product.objects
    def get_collection(self,collname):
        try:
            if collname.lower() == "all collections".lower():
                all_collections = data_index     #self.products     # data_index
                return { "collection_title":collname.title(),
                         "collectionslist":all_collections }
            else:
                all_collections=[]
                for product in self.products:
                    if product.collection.col_name.lower() == collname.lower():
                        all_collections.append(product)
                return {"collection_title": collname.title(),
                        "collectionslist": all_collections}
        except:
            all_collections=[]
            return {"collection_title": collname.title(),
             "collectionslist": all_collections}

    def get_product(self,product_id):
        try:
            product = self.product.get(id=product_id)
            return product
        except:
            return



class CartData():
    def __init__(self):
        self.cart_items = Cart.objects.all()
    def update_cart(self,product_id,product_name,product_img_url,product_type,product_size,product_quantity,product_price):
        cart_item = Cart( product_id=product_id,product_name=product_name,product_img_url=product_img_url,product_type=product_type,product_size=product_size,product_quantity=product_quantity,product_price=product_price)
        cart_item.save()

    def get_cart_items(self):
        return self.cart_items

    def count_cart_items(self):
        return self.cart_items.count()


