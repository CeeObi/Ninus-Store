from django.contrib.auth.models import User
from .models import Product, Wishlist, Purchase, Collection, Order, Cart, UserCart
from .data import data
import random
import stripe






stripe.api_key="sk_test_51O6SWXGkFiiSNOyUdkF60f3ZGLj6X6zzX9Nskb2Psxqv67Am4z6oLR30Z7STFLcNgyKi9lqWDEjzTQOr5WadfIFl00JGiUcrMa"



# data_index = []
# for index in range(0, len(data)):
#     indx = index + 1
#     data_index.append({"id":indx, "img_url":data[index],"prod_name":"white tee", "collection":{"col_name":"Jackets and tops"},"price":"199.9"})



class StoreData():
    def __init__(self):
        self.all_collections = stripe.Product.list(limit=100)
        for each in self.all_collections:
            each_price_id = each["default_price"]
            each_prices = round(((int(stripe.Price.retrieve(each_price_id)["unit_amount"])) / 100), 2)
            each["price"] = each_prices
        # self.products=Product.objects.all()
        # self.product=Product.objects
    def __str__(self):
        return "Store data up to date..."
    def get_collection(self,collname):
        try:
            if collname.lower() == "all collections".lower():
                #all_collections = data_index     #self.products     # data_index
                return { "collectionstitle":collname.title(),
                         "collectionslist":self.all_collections }
            else:
                specific_collections = []
                for each in self.all_collections:
                    if each["metadata"]["collectn_name"].lower() == collname.lower():
                        specific_collections.append(each)
                return {"collectionstitle": collname.title(),
                        "collectionslist": specific_collections}
        except:
            all_collections=[]
            return {"collection_title": collname.title(),
             "collectionslist": all_collections}
    def get_product(self,product_id):
        try:
            for each in self.all_collections:
                if each["id"] == str(product_id):
                    product = each
                    return product
        except:
            return
    def get_random_products(self,id):
        list_colctn_data=[]
        for each in self.all_collections: #Product.objects.all()
            list_colctn_data.append(each)
        random_data = random.choices(list_colctn_data, k=7)
        items_may_like = []
        for each in random_data[:6]:
            if each['id'] != id:  # changes to 'if each.id != id:' when 'storedata.product' is used above.
                each_price_id = each["default_price"]
                each_prices = round(((int(stripe.Price.retrieve(each_price_id)["unit_amount"])) / 100), 2)
                each["price"] = each_prices
                items_may_like.append(each)
        return items_may_like[:6]






class CartData():
    def __init__(self):
        pass
    def update_cart(self,product_id,product_name,product_img_url,product_type,product_size,product_quantity,product_price,product_price_id):
        cart_item = Cart( product_id=product_id,product_name=product_name,product_img_url=product_img_url,product_type=product_type,product_size=product_size,product_quantity=product_quantity,product_price=product_price,product_price_id=product_price_id)
        cart_item.save()
    def get_cart_items(self):
        return Cart.objects.all()
    def count_cart_items(self):
        return Cart.objects.count()
    def delete_cart_item(self,in_cart_id):
        Cart.objects.filter(id=in_cart_id).delete()
        return

