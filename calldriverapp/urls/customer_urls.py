from django.urls import path
from calldriverapp.views.customer import HomeTemplateView
# from calldriverapp import views
from calldriverapp.views.customer import OrderMainTemplateView

urlpatterns = [
    # path("signup/", views.SigUpView, name="sign_up"),
    # path("customerlogin/", views.CustomerLoginView, name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderMainTemplateView.as_view(), name= "order_detail"),
]