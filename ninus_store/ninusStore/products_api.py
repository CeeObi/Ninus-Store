from .models import Product,Wishlist,Purchase,Collection,Order
from .data import data, cart_items



data_index = []
for index in range(0, len(data)):
    indx = index + 1
    data_index.append({"id":indx, "img_url":data[index]})



class StoreData():
    def __init__(self):
        self.products=Product.objects.all()
    def get_collection(self,collname):
        try:
            if collname.lower() == "all".lower():
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



