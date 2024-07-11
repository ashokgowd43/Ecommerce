from django.urls import path
from . import views
 
urlpatterns = [
    
    path('', views.loginPage, name="login"),
    path('signup', views.SignupPage, name='signup'),

    path('store/', views.store, name="store"),
    path('cart/', views.cart, name="cart"),

    path('about/', views.about, name="about"),
    
    path('checkout/', views.checkout, name="checkout"),
    
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),

    path('products/', views.product, name='product'),

    path('contact/', views.contact, name='contact'),
    

]