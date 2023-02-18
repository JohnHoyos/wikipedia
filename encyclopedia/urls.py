from django.urls import path

from . import views
app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("random", views.random, name="random"),
    path("newpage", views.newpage, name="newpage"),
    path("find", views.find, name="find"),
    path("editpage", views.editpage, name="editpage"), 
    path("random", views.random, name="random"),
    path("<str:title>", views.entrypage, name="entrypage"),
      
]
