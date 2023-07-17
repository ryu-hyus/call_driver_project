from django.urls import path
from calldriverapp.views.addresshistoryCRUD import AddresshistorydataView, AddresshistorydeleteView
from calldriverapp.views.customer import HomeTemplateView, OrderDetailTemplateView
# from calldriverapp import views
from calldriverapp.views.customer import OrderMainTemplateView, OrderChangeTemplateView
from calldriverapp.views.orderdataCRUD import OrderdataView, CustomerOrderView


urlpatterns = [
    # path("signup/", views.SigUpView, name="sign_up"),
    # path("customerlogin/", views.CustomerLoginView, name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderDetailTemplateView.as_view(), name= "order_detail"),
    path("orderchange/", OrderChangeTemplateView.as_view(), name= "order_change"),
    path("orderdata/", OrderdataView.as_view(), name= "order_method"),
    path("orderdata/<int:pk>/", OrderdataView.as_view(), name= "order_method_select"), # 오더 id로 단건 조회
    path("orderdata/customer/<int:pk>/", CustomerOrderView.as_view(), name= "customer_order_method_select"), #커스토머 id로 데이터 조회 
    path("addresshistory/<int:pk>/", AddresshistorydataView.as_view(), name= "addresshistory_CRUD"), #커스토머 id로 주소 검색 기록 검색/등록
    path("addresshistory/delete/<int:pk>/", AddresshistorydeleteView.as_view(), name= "addresshistory_delete"), #히스토리 id로 삭제
]