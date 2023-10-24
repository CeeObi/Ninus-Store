from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
  path('',views.index,name="home"),
  path('catalog',views.catalog,name="catalog"),
  path('cart',views.cart,name="cart"),
  path('productdetail/<id>',views.product_detail,name="product_detail"),
  path('login',views.login,name="login"),
  path('signup',views.signup,name="signup"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)