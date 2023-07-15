from django.urls import path
from calldriverapp.views.customer import HomeTemplateView
from calldriverapp.views.member_info import login, sign_up


urlpatterns = [
    path("signup/", sign_up, name="sign_up"),
    path("login/", login, name="customer_login"),
    path("home/", HomeTemplateView.as_view(), name="home"),
]