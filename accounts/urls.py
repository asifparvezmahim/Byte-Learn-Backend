from django.urls import path
from .views import RegisterView,login_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
     path('register/', RegisterView.as_view(), name='register'),
     path('login/', login_view, name='login'),
]
