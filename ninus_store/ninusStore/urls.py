from django.urls import path,  re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
  path('',views.index,name="home"),
  path('catalog/<str:title>',views.catalog,name="catalog"),
  path('cart',views.cart,name="cart"),
  path('productdetail/<int:id>',views.product_detail,name="product_detail"),
  path('productdetail/<product_id>/<in_cart_id>',views.delete_items_cart,name="delete_items_cart"),
  path('login',views.login_pg,name="login"),
  path('registration',views.signup_pg,name="signup"),
  path('logout',views.logout_pg,name="logout"),
  path('create-checkout-session',views.create_checkout_session,name="checkout"),

]