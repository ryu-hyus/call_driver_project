from django.urls import path
from calldriverapp.views.center import OffCustomerView, OffMainView, OffTotalOrderView
from calldriverapp.views.center import CustomerListView
from calldriverapp.views.center import RealtimeOrderView
from calldriverapp.views.center import TodayOrderView
from calldriverapp.views.center import TotalOrderView
from calldriverapp.views.member_info import Staff_Logout, StaffLoginView
from calldriverapp.views.operationCRUD import OperationDaySetView, OperationOnOffView
from calldriverapp.views.realtimeorder import RealtimeOrderGetView
from calldriverapp.views.todayorderCRUD import TodayOrderGetView
from calldriverapp.views.totalorderCRUD import TotalOrderGetView

urlpatterns = [
    path("login/", StaffLoginView.as_view(), name="staff_login"),
    path("", StaffLoginView.as_view(), name="staff_login"),
    path("logout/", Staff_Logout, name="staff_logout"),
    path("customerlist/", CustomerListView.as_view(), name="customer_list_view"),
    path("realtimeorder/", RealtimeOrderView.as_view(), name="realtime_order_list"),
    path("todayorder/", TodayOrderView.as_view(), name="today_order_list"),
    path("totalorder/", TotalOrderView.as_view(), name="total_order_list"),
    path("operationonoff/", OperationOnOffView.as_view(), name="operation_onoff"),
    path("operationdayset/", OperationDaySetView.as_view(), name="operation_dayset"),
    path("offmain/", OffMainView.as_view(), name="center_main"),
    path("offcustomerlist/", OffCustomerView.as_view(), name="off_customer_list"),
    path("offtotalorder/", OffTotalOrderView.as_view(), name="off_total_order_list"),
    path("realtimeorder/get/", RealtimeOrderGetView.as_view(), name="realtime_order_get_all"),
    path("realtimeorder/get/<int:pk>/", RealtimeOrderGetView.as_view(), name="realtime_order_get_by_id"),
    path("todayorder/get/", TodayOrderGetView.as_view(), name="today_order_get_all"),
    path("todayorder/get/<int:pk>/", TodayOrderGetView.as_view(), name="today_order_get_by_id"),
    path("totalorder/get/", TotalOrderGetView.as_view(), name="total_order_get_all"),
    path("totalorder/get/<int:pk>/", TotalOrderGetView.as_view(), name="total_order_get_by_id"),

]

