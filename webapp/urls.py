
from django.urls import path
from . import views
urlpatterns = [

       path('',views.home,name=""),
       path('register',views.register, name="register"),
       path('my-login',views.my_login,name="my-login"),
       path('user-logout',views.user_logout,name="user-logout"),
       #CRUD

       #Read
       path('dashboard',views.dashboard,name="dashboard"),
       #Create
       path('create-record', views.create_record,name="create-record"),
       #update
       path('update-record/<int:pk>',views.update_record,name='update-record'),
       #view
       path('record/<int:pk>',views.singular_record,name='singular_record'),
       #delete
       path('delete-record/<int:pk>',views.delete_record,name="delete-record")



       



]