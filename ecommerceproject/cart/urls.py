from django.urls import path, re_path
from . import views

app_name = 'cart'
urlpatterns = [
    path('', views.Cart_detail, name='Cart_detail'),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    #re_path(r'^.*/cart/', views.Cart_detail, name='cart_detail'),

    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('full_remove/<int:product_id>/', views.full_remove, name='full_remove'),
]
