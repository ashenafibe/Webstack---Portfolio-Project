from django.urls import path
from . import views
from .import HodViews,OperationView,FinanceView,ManagerView,ClientView

urlpatterns = [
 
    path ('client-request/',views.client_req,name='client_req'),
    path ('success/',views.success, name='seccess'),
    path('search/', views.search_post, name='search-view'),
    path('searchreq/',views.search_form, name='search_form'),
    path('customer_request/<int:pk>',views.customer_request,name='customer_request'),
    path('update_request/<int:pk>',views.update_request,name='update-request'),
    path('print_record/<int:pk>',views.print_record, name="print_record"),
    path('client',ClientView.Client_Home,name='home_client'),
    # staff for 
    path('', views.loginPage, name="login"),
    path('doLogin/', views.doLogin, name="doLogin"),
    path('get_user_details/', views.get_user_details, name="get_user_details"),
    path('logout_user/', views.logout_user, name="logout_user"),

    #Admin page
    path('admin_home/', HodViews.admin_home, name="admin_home"),
   
    path('finance_home/', FinanceView.finance_home, name="finance_home"),
    #path('manager_home/', ManagerView.Manager_home, name="manager_home"),
    path('add_client/',HodViews.add_client,name="add_client"),
    path('add_operation/',HodViews.add_operation, name="add_operation"),
    path('add_operation_save/',HodViews.add_operation_save,name="add_operation_save"),
    path('manage_operation',HodViews.manage_operation,name="manage_operation"),
    path('edit_operation/<operation_id>',HodViews.edit_operation,name ="edit_operation"),
    path('add_client_save/',HodViews.add_saveclient_save,name="add_client_save"),
    path('check_email_exist/', HodViews.check_email_exist, name="check_email_exist"),
    path('check_username_exist/', HodViews.check_username_exist, name="check_username_exist"),
    path('manage_client',HodViews.manage_client,name="manage_client"),
    path('edit_client/<client_id>/', HodViews.edit_client, name="edit_client"),

    path ('add_manager/',HodViews.add_managers, name="add_manager"),
    path('manage_manager/',HodViews.manage_operation, name= "manage_manager"),
    path('add_manager_save/',HodViews.add_manager_save,name="add_manager_save"),

   #operation
   #path('manage_request/',OperationView.manage_request,name="manage_request"),
  # path ('operation_home/',OperationView.operation_home,name="operation_home"),
   path ('current_page/',views.current_page,name="current_page"),
   path ('manage_request/',views.manage_requests,name="manage_request"),
   path('viewclient_details/<request_id>/',views.viewclient_details,name="viewclient_details"),
   path('edit_request/<request_id>/',views.edit_requests,name="edit_request"),

   path('manager_home/',views.current_page_manager,name="manager_home"),
   path('manage_request_manager/',views.manage_requests_manager,name="manage_request_manager"),
   path('edit_request_manager/<request_id>/',views.edit_requests_manager,name="edit_request_manager"),
   path('viewclient_details/<request_id>/',views.viewclient_details,name="viewclient_details")



 

    
   

    # c

    
]