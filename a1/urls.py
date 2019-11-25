from django.contrib import admin
from django.urls import path,include
from .import views
urlpatterns = [
    path("",views.homepage,name="homepage"),
    path("logIndata",views.datapage,name="getdata"),
    path("displaydata",views.showdata,name="display"),
    path("editdata",views.edit,name="editdata"),
    path("updated",views.change,name="updated"),
    
    path("deleted",views.delete,name="deleted")
   ]