from django.urls import path

from calldriverapp.views.center import MainView
from calldriverapp.views.center import CustomerListView
from calldriverapp.views.center import RealtimeOrderView
from calldriverapp.views.center import TodayOrderView
from calldriverapp.views.center import TotalOrderView
from calldriverapp.views.member_info import StaffLoginView

urlpatterns = [
    path("", StaffLoginView.as_view(), name="superuser_login"),
    path("main/", MainView.as_view(), name="center_main"),
    path("customerlist/", CustomerListView.as_view(), name="customer_list_view"),
    path("realtimeorder/", RealtimeOrderView.as_view(), name="realtime_order_list"),
    path("todayorder/", TodayOrderView.as_view(), name="today_order_list"),
    path("totalorder/", TotalOrderView.as_view(), name="total_order_list"),
]