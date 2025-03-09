from django.urls import path
from .views.register_view import RegisterView
from .views.login_view import LoginView
from .views.recovery_view import RecoveryPasswordView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('recovery-password/', RecoveryPasswordView.as_view(), name='recovery_password'),
]


