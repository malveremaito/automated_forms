from sre_constants import SUCCESS
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('change_password/',
    auth_views.PasswordChangeView.as_view(
        template_name='change_password.html',
        success_url='/accounts/logout'),
    name='change-password')
]
