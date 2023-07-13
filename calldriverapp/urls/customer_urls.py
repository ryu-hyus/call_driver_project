from django.urls import path
from calldriverapp.views.customer import HomeTemplateView, SigUpView, CustomerLoginView
from calldriverapp import views

urlpatterns = [
    path("signup/", SigUpView.as_view(), name="sign_up"),
    path("customerlogin/", CustomerLoginView.as_view(), name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home")
]