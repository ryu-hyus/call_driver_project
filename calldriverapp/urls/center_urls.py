from django.urls import path
from calldriverapp.views.center import OffCustomerView, OffMainView, OffTotalOrderView
from calldriverapp.views.center import CustomerListView
from calldriverapp.views.center import RealtimeOrderView
from calldriverapp.views.center import TodayOrderView
from calldriverapp.views.center import TotalOrderView
from calldriverapp.views.member_info import StaffLoginView
from calldriverapp.views.operationCR import OperationOnOffView
from calldriverapp.views.realtimeorder import RealtimeOrderGetView

urlpatterns = [
    path("", StaffLoginView.as_view(), name="superuser_login"),
    path("customerlist/", CustomerListView.as_view(), name="customer_list_view"),
    path("realtimeorder/", RealtimeOrderView.as_view(), name="realtime_order_list"),
    path("todayorder/", TodayOrderView.as_view(), name="today_order_list"),
    path("totalorder/", TotalOrderView.as_view(), name="total_order_list"),
    path("operationonoff/", OperationOnOffView.as_view(), name="operation_onoff"),
    path("offmain/", OffMainView.as_view(), name="center_main"),
    path("offcustomerlist/", OffCustomerView.as_view(), name="off_customer_list"),
    path("offtotalorder/", OffTotalOrderView.as_view(), name="off_total_order_list"),
    path("realtimeorder/get/", RealtimeOrderGetView.as_view(), name="realtime_order_get"),
]

