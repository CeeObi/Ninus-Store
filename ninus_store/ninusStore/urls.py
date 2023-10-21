from django.urls import path
from . import views

urlpatterns=[
  path('',views.index,name="home"),
  path('catalog',views.catalog,name="catalog"),
  path('detail-x',views.product_detail,name="product-x"),

]