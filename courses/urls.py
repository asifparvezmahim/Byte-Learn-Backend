# yourapp/urls.py
from django.urls import path
from .views import create_category,list_categories,create_course,list_courses,create_course_module,list_course_modules,create_course_video,list_course_videos

urlpatterns = [
    path('create-course-categories/', create_category, name='category-create'),
    path('categories/', list_categories, name='list-categories'),
    path('create-course/', create_course, name='course-create'),
    path('courses/', list_courses, name='course-list'),
    path('create-course-module/', create_course_module, name='module-create'),
    path('course-modules/', list_course_modules, name='list-course-modules'),
    path('create-course-video/', create_course_video, name='video-create'),
    path('course-videos/', list_course_videos, name='list-course-videos'),
]
