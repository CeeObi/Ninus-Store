import random

import stripe

stripe.api_key="sk_test_51O6SWXGkFiiSNOyUdkF60f3ZGLj6X6zzX9Nskb2Psxqv67Am4z6oLR30Z7STFLcNgyKi9lqWDEjzTQOr5WadfIFl00JGiUcrMa"
cart_items={
    "1":{
        "Quantity":2,
        "product_name": "Tee White",
        "Description": "Lorem ipsum dolor sit amet."
    }
}


data =["https://images.unsplash.com/photo-1683849117195-83517b362436?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTI4fHx3aGl0ZSUyMGJhY2tncm91bmQlMjB3b21lbiUyMGZhc2hpb258ZW58MHx8MHx8fDA%3D",
"https://images.unsplash.com/photo-1630255733678-cf82ac59eef8?auto=format&fit=crop&q=60&w=500&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MjI0fHx3aGl0ZSUyMGJhY2tncm91bmQlMjB3b21lbiUyMGZhc2hpb258ZW58MHx8MHx8fDA%3D",
"https://images.pexels.com/photos/7290682/pexels-photo-7290682.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/13221803/pexels-photo-13221803.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/4411905/pexels-photo-4411905.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/15576198/pexels-photo-15576198/free-photo-of-woman-with-black-hair-posing.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/3774935/pexels-photo-3774935.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/8317648/pexels-photo-8317648.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6480701/pexels-photo-6480701.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/1958744/pexels-photo-1958744.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6702737/pexels-photo-6702737.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7872818/pexels-photo-7872818.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7691354/pexels-photo-7691354.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/17905263/pexels-photo-17905263/free-photo-of-brunette-woman-in-white-shirt-mini-skirt-and-tie-sitting-on-white-pedestals.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/5411876/pexels-photo-5411876.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6311268/pexels-photo-6311268.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/9456640/pexels-photo-9456640.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/9558765/pexels-photo-9558765.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/2474257/pexels-photo-2474257.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7289124/pexels-photo-7289124.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7205291/pexels-photo-7205291.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6995868/pexels-photo-6995868.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6995871/pexels-photo-6995871.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7088625/pexels-photo-7088625.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6945667/pexels-photo-6945667.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/12883668/pexels-photo-12883668.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/9573706/pexels-photo-9573706.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/2085521/pexels-photo-2085521.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6311249/pexels-photo-6311249.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/15502859/pexels-photo-15502859/free-photo-of-woman-posing-in-black-hat.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/10839230/pexels-photo-10839230.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/10655897/pexels-photo-10655897.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/4621787/pexels-photo-4621787.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/3765976/pexels-photo-3765976.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6702631/pexels-photo-6702631.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6311578/pexels-photo-6311578.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/2703181/pexels-photo-2703181.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6975251/pexels-photo-6975251.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6945617/pexels-photo-6945617.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6702720/pexels-photo-6702720.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7203448/pexels-photo-7203448.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7690953/pexels-photo-7690953.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/15522601/pexels-photo-15522601/free-photo-of-blonde-woman-with-backpack.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/17146259/pexels-photo-17146259/free-photo-of-young-brunette-in-a-black-bodysuit-posing-in-studio.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/14164323/pexels-photo-14164323.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6702719/pexels-photo-6702719.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/8728098/pexels-photo-8728098.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6995860/pexels-photo-6995860.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/9768430/pexels-photo-9768430.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/7203743/pexels-photo-7203743.jpeg?auto=compress&cs=tinysrgb&w=600",
"https://images.pexels.com/photos/6311274/pexels-photo-6311274.jpeg?auto=compress&cs=tinysrgb&w=600",
]


#
# #
# data_index = []
# for index in range(0, len(data)):
#     indx = index + 1
#     print(data[index])
#     stripe.Product.create(id=indx,name="White Tee",metadata={"collectn_name":"Jackets and tops"}, description=f"{indx}", images=[data[index]], default_price_data = {"unit_amount_decimal":"19995", "currency":"aud"},url=data[index])
#     #stripe.Product.delete(f"{indx}")
# product=stripe.Product.retrieve("1")
# each_price_id = product["default_price"]
# each_prices = round(((int(stripe.Price.retrieve(each_price_id)["unit_amount"])) / 100), 2)
# product["price"] = each_prices
# print(product)

# product=stripe.Product.search(query="metadata['collectn_name']:'Jackets and tops'",limit=20)
# print(len(product))
#
# collections_name="Jackets and tops"
# product=stripe.Product.search(query=f"metadata['collectn_name']: '{collections_name}'",limit=20)
# print(len(product))


# #
# price=stripe.Price.retrieve("price_1O6nPjGkFiiSNOyUN2zhaWON")
# print(price)
# colctn_data = stripe.Product.list(limit=5)
# list_colctn_data=[]
# for each in colctn_data: #Product.objects.all()
#     list_colctn_data.append(each)
# print(list_colctn_data)
# # random_data = random.choices(all_products, k=7)
# print(type(random_data))
