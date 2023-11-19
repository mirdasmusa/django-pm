from django.urls import path,include
from django.contrib.auth.views import LoginView
from accounts.forms import UserLoginForm
from accounts.views import RegisterView, edit_profile
from django.conf.urls.i18n import i18n_patterns

urlpatterns =[
    path('login/', LoginView.as_view(authentication_form=UserLoginForm), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', edit_profile, name='profile'),
    path('', include('django.contrib.auth.urls')),

]