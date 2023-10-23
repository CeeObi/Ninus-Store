from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name="home"),
  path('catalog',views.catalog,name="catalog"),
  path('catalog2',views.catalog2,name="catalog2"),
  path('productdetail/<id>',views.product_detail,name="product_detail"),

]