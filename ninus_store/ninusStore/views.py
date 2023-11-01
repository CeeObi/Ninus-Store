from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
# from .products_api import StoreData, CartData
# from .products_api_stripe import StoreData, CartData,stripe
from .products_api_stripe_modified import StoreData, CartData,stripe
# import requests



storedata = StoreData() #initializes store data in products_api
cartdata = CartData()

YOUR_DOMAIN = 'https://localhost:8000'


# # @app.route('/create-checkout-session', methods=['POST'])



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
    context["collection_title"] = product_collection["collectionstitle"].title()
    context["cart_items"] = cartdata.get_cart_items()
    context["no_of_cart_items"] = cartdata.count_cart_items()
    return render(request,"catalog.html",context=context)


def cart(request):
    return render(request,"cart.html")


def product_detail(request,id):
    context={}
    id = int(id)
    spec_product = storedata.get_product(product_id=id)
    # For the GET method
    context["spec_product"] = spec_product
    context["cntx_data"] = storedata.get_random_products(id=id)
    context["cart_items"] = cartdata.get_cart_items()
    context["no_of_cart_items"] = cartdata.count_cart_items()
    if request.method == "POST":
        product_id = id
        product_name = spec_product.name
        product_img_url = spec_product.url
        product_type = request.POST.get("options")
        product_size = request.POST.get("product_size")
        product_quantity = request.POST.get("quantity")
        product_price = spec_product.price
        product_price_id = spec_product.default_price
        cartdata.update_cart( product_id= product_id,product_name=product_name,product_img_url=product_img_url,product_type=product_type,product_size=product_size,product_quantity=product_quantity,product_price=product_price,product_price_id=product_price_id)
        context["cart_items"] = cartdata.get_cart_items()
        context["no_of_cart_items"] = cartdata.count_cart_items()
        return render(request,"product_detail.html", context=context)
    return render(request,"product_detail.html", context=context)



def delete_items_cart(request,product_id,in_cart_id):
    context={}
    id = int(product_id)
    in_cart_id=in_cart_id
    cartdata.delete_cart_item(in_cart_id)
    #Query Products
    spec_product = storedata.get_product(product_id=id)
    context["spec_product"] = spec_product
    context["cntx_data"] = storedata.get_random_products(id=id)
    context["cart_items"] = cartdata.get_cart_items()
    context["no_of_cart_items"] = cartdata.count_cart_items()
    return render(request,"product_detail.html", context=context)



def create_checkout_session(request):
    try:
        global storedata
        storedata = StoreData()
        present_cart_items = cartdata.get_cart_items()
        line_items = []
        for cart_item in present_cart_items:
            price_id= cart_item.product_price_id
            quantity=int(cart_item.product_quantity)
            each_line_purchased = {'price': price_id,'quantity': quantity}
            line_items.append(each_line_purchased)
        checkout_session = stripe.checkout.Session.create(
            line_items=line_items,
            mode='payment',
            success_url=YOUR_DOMAIN + '/checkout.html',
            cancel_url=YOUR_DOMAIN + '/cancel.html',
        )
    except Exception as e:
        return str(e)
    return redirect(checkout_session.url, code=303)






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

