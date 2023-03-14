from . import views
from django.urls import path

app_name = 'admin'

urlpatterns = [
    path('home',views.admin,name='admin_home'),
    path('',views.admin_login,name='admin_login'),
    path('add_product',views.add_product,name='add_product'),
    path('prod_details/<int:pid>',views.prod_details,name='prod_details'),
    path('add_variant/<int:pid>',views.add_variant,name='add_variant'),
    path('logout',views.logout,name='logout'),

]