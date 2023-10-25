from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from werkzeug.security import generate_password_hash
from django.contrib import messages

from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from .data import data, cart_items
import random





data_index = []
for index in range(0, len(data)):
    indx = index + 1
    data_index.append({"id":indx, "url":data[index]})



def index(request):
    return render(request,"home.html")


#print(data)

def catalog(request):
    context={}
    login = LoginForm
    signup = SignUpForm
    #global data
    context["cntx_data"]=data_index
    context["login"] = login
    context["signup"] = signup
    return render(request,"catalog.html",context=context)

def cart(request):
    return render(request,"cart.html")

def product_detail(request,id):
    context={}
    data_reduced=data_index
    id = int(id)
    for item in data_index:
        if item["id"]==id:
            idz_url=item["url"]
            context["cntx_url"] = idz_url
    random_data= random.choices(data_reduced, k=7)
    for each in random_data[:6]:
        if each["id"] == id:
            indx=random_data.index(each)
            random_data.pop(indx)
    context["cntx_data_reduced"] = random_data[:6]
    return render(request,"product_detail.html", context=context)


def login_pg(request):
    logn=LoginForm
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user_exist = User.objects.filter(username=username).exists()
            if user_exist:
                hashed_password = password
                print(hashed_password)
                user = authenticate(request, username=username, password=hashed_password)
                # user = User.objects.get(username=username)
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
                hashed_password = make_password(password)
                user = User.objects.create_user(first_name=firstname, last_name=lastname, username=username, email=email, password=hashed_password)
                login(request, user)
                return HttpResponseRedirect(reverse("home"))
        except User.DoesNotExist:
            return render(request, "signup.html", context={"signup": signup})
    return render(request, "signup.html", context={"signup": signup})


def logout_pg(request):
    logout(request)
    return HttpResponseRedirect(reverse("home"))

