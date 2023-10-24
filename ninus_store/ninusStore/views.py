from django.shortcuts import render
from .forms import LoginForm, SignUpForm
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
    #global data
    context["cntx_data"]=data_index
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


def login(request):
    login=LoginForm
    return render(request,"login.html",context={"forms": login})



def signup(request):
    signup=SignUpForm
    return render(request,"signup.html",context={"forms": signup})

