from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegistrationView

urlpatterns = [
    path('login/token/', TokenObtainPairView.as_view()),
    path('login/token/refresh/', TokenRefreshView.as_view()),
    path('register/', RegistrationView.as_view())
]