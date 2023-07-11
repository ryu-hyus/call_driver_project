from django.urls import path

urlpatterns = [
    path("superuserlogin/", SuperuserLoginView.as_view(), name="superuser_login"),
    path("customerlist/", CustomerListView.as_view(), name="customer_list_view"),
    path("realtimeorder/", RealtimeOrderView.as_view(), name="realtime_order_list"),
    path("todayorder/", TodayOrderView.as_view(), name="today_order_list"),
    path("totalorder/", TotalOrderView.as_view(), name="total_order_list"),
]