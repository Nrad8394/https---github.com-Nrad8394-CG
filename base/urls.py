from django.urls import path
from . import views

urlpatterns = [
    path('add_transporter/', views.add_transporter,name='add_transporter'),
    path('add_transporter_save/', views.add_transporter_save,name='add_transporter_save'),
    path('add_item/', views.add_item,name='add_item'),
    path('add_item_save/', views.add_item_save,name='add_item_save'),
    path('add_order/', views.add_order,name='add_order'),
    path('add_order_save/', views.add_order_save,name='add_order_save'),
     path('', views.tracker, name="tracker"),

    path('check_email_exist/', views.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', views.check_username_exist, name="check_username_exist"),
    
]
