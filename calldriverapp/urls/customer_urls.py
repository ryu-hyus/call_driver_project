from django.urls import path
from calldriverapp.views.addresshistoryCRUD import AddresshistorydataView, AddresshistorydeleteView
from calldriverapp.views.customer import HomeTemplateView, MapExamView, OrderDetailTemplateView, OrderDetailTemplateView, SearchAddress
from calldriverapp.views.customer import OrderMainTemplateView
from calldriverapp.views.member_info import CustomerLoignView, SignUpView
from calldriverapp.views.customer import OrderMainTemplateView, OrderChangeTemplateView
from calldriverapp.views.orderdataCRUD import OrderdataView, CustomerOrderView
from calldriverapp.views.pricecaculate import PriceTableView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("login/", CustomerLoignView.as_view(), name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderDetailTemplateView.as_view(), name= "order_detail"),
    path("orderchange/", OrderChangeTemplateView.as_view(), name= "order_change"),
    path("orderdata/", OrderdataView.as_view(), name= "order_method"),
    path("orderdata/<int:pk>/", OrderdataView.as_view(), name= "order_method_select"), # 오더 id로 단건 조회
    path("orderdata/customer/<int:pk>/", CustomerOrderView.as_view(), name= "customer_order_method_select"), #커스토머 id로 데이터 조회 
    path("addresshistory/<int:pk>/", AddresshistorydataView.as_view(), name= "addresshistory_CRUD"), #커스토머 id로 주소 검색 기록 검색/등록
    path("addresshistory/delete/<int:pk>/", AddresshistorydeleteView.as_view(), name= "addresshistory_delete"), #히스토리 id로 삭제
    path("mapexam/", MapExamView.as_view(), name= "map_exam"),
    path("searchaddress/", SearchAddress.as_view(), name= "search_address"),
    path("pricecalculate/<str:ss>/<str:es>/", PriceTableView.as_view(), name= "calculate_price"), # 요금 계산 url / ss: 출발지, es: 도착지로 검색
]