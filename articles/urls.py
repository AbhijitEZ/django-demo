from django.contrib import admin
from django.urls import path
from .views import index_view, add_view, detail_view, delete, edit_view
urlpatterns = [
    path('', index_view, name='index'),
    path('add/', add_view, name='add'),
    path('detail/<int:id>', detail_view, name='detail'),
    path('delete/<int:id>', delete, name='delete'),
    path('edit/<int:id>', edit_view, name='edit')


]
