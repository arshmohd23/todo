from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('update/<int:id>', views.updatetask, name='update'),


    path('delete/<int:id>', views.deletetask, name='delete'),

    path('delete_all', views.deleteall, name='deleteall'),


]
