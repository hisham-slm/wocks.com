from . import views
from django.urls import path

app_name = 'customer'

urlpatterns = [
    path('',views.home_page,name='home_page'),
    path('login',views.login_page,name='login'),
    path('signup',views.signup_page,name='signup'),
    path('shoes',views.shoes,name='shoespage'),
    path('prod_details/<int:pid>',views.prod_details,name='prod_details'),
    path('email_exist',views.email_exist, name='email_exist'),
    path('logout',views.logout, name='logout'),
    path('watches',views.watches, name='watches'),
    path('add_to_cart',views.add_to_cart, name='add_to_cart'),
    path('review/<int:pid>',views.review, name='review'),



]