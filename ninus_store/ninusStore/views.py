from django.contrib.auth import login,authenticate,logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib import messages
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from .products_api import StoreData
import random

storedata = StoreData() #initializes store data in products_api


def index(request):
    return render(request,"home.html")


def catalog(request):
    context={}
    login = LoginForm
    signup = SignUpForm

    #collname="Jackets and Tops"
    collname = "all collections"

    product_collection = storedata.get_collection(collname=collname) #has been initialized above
    context["cntx_data"]=product_collection["collectionslist"]
    context["login"] = login
    context["signup"] = signup
    context["collection_title"] = product_collection["collection_title"].title()
    return render(request,"catalog.html",context=context)


def catalog_collections(request):
    context={}
    login = LoginForm
    signup = SignUpForm

    #collname="Jackets and Tops"
    collname = "all collections"

    product_collection = storedata.get_collection(collname=collname) #has been initialized above
    context["cntx_data"]=product_collection["collectionslist"]
    context["login"] = login
    context["signup"] = signup
    context["collection_title"] = product_collection["collection_title"].title()
    return render(request,"catalog.html",context=context)


def cart(request):
    return render(request,"cart.html")


def product_detail(request,id):
    context={}
    product_collection = storedata.get_collection(collname="all collections")
    colctn_data=product_collection["collectionslist"]
    id = int(id)
    for item in colctn_data:
        if item["id"]==id:
            idz_url=item["img_url"]
            context["cntx_img_url"] = idz_url
    random_data= random.choices(colctn_data, k=7)
    for each in random_data[:6]:
        if each["id"] == id:
            indx=random_data.index(each)
            random_data.pop(indx)
    context["cntx_data"] = random_data[:6]

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

