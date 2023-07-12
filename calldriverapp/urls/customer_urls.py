from django.urls import path
from calldriverapp.views import HomeTemplateView

urlpatterns = [
    # path("signup/", SigUpView.as_view(), name="sign_up"),
    # path("customerlogin/", CustomerLoginView.as_view(), name="customer_login"),
    # path("customerinfo/", CustomerInfoView.as_view(), name="customer_information"),
    # path("getorder/", GetOrderView.as_view(), name="get_order"),
    # path("confirmorder/", ConfirmOrderView.as_view(), name="confirm_order"),
    # path("changeorder/", ChangeOrderView.as_view(), name="change_order"),
    # # 주소는 api 연결?
    # path("setaddress/", SetAddressView.as_view(), name="set_adress"),
    # path("pricetable/", PriceTableView.as_view(), name="price_table"),
    path("home/", HomeTemplateView.as_view(), name="home")
]
