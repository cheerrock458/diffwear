<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_product, name='add_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add-product/', views.add_product, name='add_product'),
    path('checkout/', views.checkout, name='checkout'),
    path('chat/', views.chat_list, name='chat_list'),
    path('chat/<int:id>/', views.chat_detail, name='chat_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('seller-inbox/', views.seller_inbox, name='seller_inbox'),
    path('buy-now/<int:id>/', views.buy_now, name='buy_now'),   
=======
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add/', views.add_product, name='add_product'),
    path('delete/<int:id>/', views.delete_product, name='delete_product'),

    path('cart/', views.cart, name='cart'),
    path('add-to-cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:id>/', views.remove_from_cart, name='remove_from_cart'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('add-product/', views.add_product, name='add_product'),
    path('checkout/', views.checkout, name='checkout'),
    path('chat/', views.chat_list, name='chat_list'),
    path('chat/<int:id>/', views.chat_detail, name='chat_detail'),
    path('checkout/', views.checkout, name='checkout'),
    path('seller-inbox/', views.seller_inbox, name='seller_inbox'),
    path('buy-now/<int:id>/', views.buy_now, name='buy_now'),   
>>>>>>> 8ada485e1e7684880b2e8dfde05d8b4234635a24
]