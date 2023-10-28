from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from .products_api import StoreData, CartData
import random

storedata = StoreData() #initializes store data in products_api
cartdata = CartData()

def index(request):
    return render(request,"home.html")


def catalog(request,title):
    context={}
    login = LoginForm
    signup = SignUpForm
    product_collection = storedata.get_collection(collname=title) #has been initialized above, "Jackets and Tops", "all collections"
    context["cntx_data"]=product_collection["collectionslist"]
    context["login"] = login
    context["signup"] = signup
    context["collection_title"] = product_collection["collection_title"].title()
    return render(request,"catalog.html",context=context)


def cart(request):
    return render(request,"cart.html")


def product_detail(request,id):
    context={}
    spec_product = storedata.get_product(product_id=id)
    colctn_data=storedata.get_collection(collname="all collections")["collectionslist"] #should use 'storedata.products' only, but it is not presently populated at the admin.
    id = int(id)
    # For the GET method
    context["spec_product"] = spec_product
    random_data = random.choices(colctn_data, k=7)
    items_may_like = []
    for each in random_data[:6]:
        if each['id'] != id:  # changes to 'if each.id != id:' when 'storedata.product' is used above.
            items_may_like.append(each)
    context["cntx_data"] = items_may_like[:6]

    if request.method == "POST":
        product_id = id
        product_name = spec_product.prod_name
        product_img_url = spec_product.img_url
        product_type = request.POST.get("options")
        product_size = request.POST.get("product_size")
        product_quantity = request.POST.get("quantity")
        product_price = spec_product.price
        print(type(product_price))
        username = request.user.username
        cartdata.update_cart( product_id= product_id,product_name=product_name,product_img_url=product_img_url,product_type=product_type,product_size=product_size,product_quantity=product_quantity,product_price=product_price)
        context["cart_items"] = cartdata.get_cart_items()
        context["no_of_cart_items"]=cartdata.count_cart_items()
        print(context["no_of_cart_items"])
        return render(request,"product_detail.html", context=context)
    return render(request,"product_detail.html", context=context)


def login_pg(request):
    logn=LoginForm
    if request.method == "POST":
        usernme = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_exist = User.objects.filter(username=usernme).exists()
            if user_exist:
                username = User.objects.get(username=usernme)
                user = authenticate(request, username=username, password=password)
                # if user.check_password(password): #Another way to authenticate
                if user is not None:
                    login(request,user)
                    return HttpResponseRedirect(reverse("home"))
                else:
                    messages.error(request, 'Incorrect login details.')
                    return HttpResponseRedirect(reverse("login"))
            else:
                messages.error(request, 'User does not exist. Please signup!')
                return HttpResponseRedirect(reverse("signup"))
        except User.DoesNotExist:
            return render(request, "login.html", context={"login": logn})
    return render(request, "login.html", context={"login": logn})


def signup_pg(request):
    signup=SignUpForm
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        try:
            email_exist = User.objects.filter(email=email).exists()
            user_exist = User.objects.filter(username=username).exists()
            if user_exist or email_exist:
                messages.error(request, 'User already exist.')
                return HttpResponseRedirect(reverse("login"))
            else:
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=password)
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
        except User.DoesNotExist:
            return render(request, "signup.html", context={"signup": signup})
    return render(request, "signup.html", context={"signup": signup})


def logout_pg(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

