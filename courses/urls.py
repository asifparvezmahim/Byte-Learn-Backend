# yourapp/urls.py
from django.urls import path
from .views import create_category,list_categories

urlpatterns = [
    path('create-course-categories/', create_category, name='category-create'),
    path('categories/', list_categories, name='list-categories')
]
