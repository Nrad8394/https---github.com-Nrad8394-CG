from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view , name='login'),
    path('base/', views.base , name='base'),
    path('tracker/',views.tracker,name='tracker'),
    path('add_transporter/', views.add_transporter,name='add_transporter'),
    path('add_transporter_save/', views.add_transporter_save,name='add_transporter_save'),
    path('items/', views.items,name='items'),
    path('add_item/', views.add_item,name='add_item'),
    path('add_item_save/', views.add_item_save,name='add_item_save'),
    path('search/',views.search_item,name='search_item'),
    

    path('new_entry/<str:item_id>', views.new_entry,name='new_entry'),
    path('new_entry_save/<str:item_id>', views.new_entry_save,name='new_entry_save'),
    path('print-order/<str:unique_code>/', views.print_order, name='print_order'),
    path('tracking/', views.tracker, name="tracker"),
    path('check_email_exist/', views.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', views.check_username_exist, name="check_username_exist"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('logout_user/', views.logout_user, name="logout_user"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),

    path('profile/', views.profile, name="profile"),
    path('profile_update/', views.profile_update, name="profile_update"),
    
]
