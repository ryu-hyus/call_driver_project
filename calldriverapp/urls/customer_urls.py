from django.urls import path
from calldriverapp.views.addresshistoryCRUD import AddresshistorydataView, AddresshistorydeleteView, EndAddresshistorydataView, StartAddresshistorydataView
from calldriverapp.views.customer import HomeTemplateView, OrderDetailTemplateView, OrderDetailTemplateView

from calldriverapp.views.customer import OrderMainTemplateView
from calldriverapp.views.member_info import CustomerLoignView, FindIdView, Customer_Logout, MyPageView, SignUpView, check_username, update_profile
from calldriverapp.views.customer import OrderMainTemplateView, OrderChangeTemplateView, PricePageView, TermsView
from calldriverapp.views.orderdataCRUD import OrderdataView, CustomerOrderView
from calldriverapp.views.pricecaculate import PriceTableView
from calldriverapp.views.myuserCRUD import CustomerInfoView


urlpatterns = [
    path("signup/", SignUpView.as_view(), name="sign_up"),
    path("check_username/", check_username, name="check_username"),
    path("login/", CustomerLoignView.as_view(), name="customer_login"),
    path("logout/", Customer_Logout, name="customer_logout"),
    path("find_id/", FindIdView.as_view(), name="find_id"),
    path("home/", HomeTemplateView.as_view(), name="home"),
    path("mypage/", MyPageView.as_view(), name="mypage"),
    path("mypage/update_profile/", update_profile, name="update_profile"),
    path("customer_info/", CustomerInfoView.as_view(), name="customer_info_select"),
    path("customer_info/<int:pk>/", CustomerInfoView.as_view(), name="customer_info_select"),
    path("ordermain/", OrderMainTemplateView.as_view(), name= "order_main"),
    path("orderdetail/", OrderDetailTemplateView.as_view(), name= "order_detail"),
    path("orderchange/", OrderChangeTemplateView.as_view(), name= "order_change"),
    path("orderdata/", OrderdataView.as_view(), name= "order_method"),
    path("orderdata/<int:pk>/", OrderdataView.as_view(), name= "order_method_select"), # 오더 id로 단건 조회
    path("userorder/<int:pk>/", CustomerOrderView.as_view(), name= "customer_order_method_select"), #커스토머 id로 데이터 조회 
    path("addresshistory/<int:pk>/", AddresshistorydataView.as_view(), name= "addresshistory_CRUD"), #커스토머 id로 주소 검색 기록 검색/등록
    path("addresshistory/start/<int:pk>/", StartAddresshistorydataView.as_view(), name= "startaddresshistory_get"), #커스토머 id 출발지 검색 기록 검색/등록
    path("addresshistory/end/<int:pk>/", EndAddresshistorydataView.as_view(), name= "endaddresshistory_get"), #커스토머 id 목적지 검색 기록 검색/등록
    path("addresshistory/delete/<int:pk>/", AddresshistorydeleteView.as_view(), name= "addresshistory_delete"), #히스토리 id로 삭제
    path("pricecalculate/<str:ss>/<str:es>/", PriceTableView.as_view(), name= "calculate_price"), # 요금 계산 url / ss: 출발지, es: 도착지로 검색
    path("pricepage/", PricePageView.as_view(), name= "pricepage"), #요금표 페이지
    path("terms/", TermsView.as_view(), name= "terms"), #개인정보방침, 위치기록 페이지
]