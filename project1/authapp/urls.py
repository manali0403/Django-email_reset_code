from django.urls import path
from . import views

urlpatterns = [
    path('rv/',views.register_view,name = 'signup_url'),
    path('lv/',views.login_view,name = 'login_url'),
    path('lo/',views.logout_view,name = 'logout_url'),
    path('ev/',views.reset_password_form_view,name='email_url')
]