from django.urls import path
from calldriverapp.views import HomeTemplateView
from calldriverapp import views

urlpatterns = [
    path("signup/", views.SigUpView, name="sign_up"),
    path("customerlogin/", views.CustomerLoginView, name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home")
    #kkk
]