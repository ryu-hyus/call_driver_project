from django.urls import path
from calldriverapp.views.customer import HomeTemplateView, OrderDetailTemplateView
from calldriverapp import views
from calldriverapp.views.customer import OrderMainTemplateView, OrderChangeTemplateView
from calldriverapp.views.orderdataCRUD import OrderdataView, CustomerOrderView

urlpatterns = [
    # path("signup/", SigUpView.as_view(), name="sign_up"),
    # path("customerlogin/", CustomerLoginView.as_view(), name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderDetailTemplateView.as_view(), name= "order_detail"),
    path("orderchange/", OrderChangeTemplateView.as_view(), name= "order_change"),
    path("orderdata/", OrderdataView.as_view(), name= "order_method"),
    path("orderdata/<int:pk>", OrderdataView.as_view(), name= "order_method_select"), # 오더 id로 단건 조회
    path("orderdata/customer/<int:pk>", CustomerOrderView.as_view(), name= "customer_order_method_select"), #커스토머 id로 데이터 조회 
]