from django.urls import path

from user.views import (LoginView,
                        RegistrationView)

urlpatterns = [
    path('registration/', RegistrationView.as_view(), name='registration'),
    path('login/', LoginView.as_view(), name='login'),
]
