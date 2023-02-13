from django.urls import path
from . import views
urlpatterns = [
    path('login/',views.Loginpage,name="Loginpage"),
    path('signup/',views.signup,name="signup"),
    path('password/',views.PasswordPage,name="password"),
    path('forgot_otp/',views.forgot_otp,name="forgot_otp"),
    path('forgot_password/',views.forgot_pass,name="forgot_pass"),
    path('new_pass/',views.new_pass,name="new_pass"),
]