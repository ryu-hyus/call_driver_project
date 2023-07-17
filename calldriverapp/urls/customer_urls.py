from django.urls import path
from calldriverapp.views.customer import HomeTemplateView, OrderDetailTemplateView
from calldriverapp.views.customer import OrderMainTemplateView
from calldriverapp.views.member_info import CustomerLoignView, SignUpView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("login/", CustomerLoignView.as_view(), name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderDetailTemplateView.as_view(), name= "order_detail"),
]