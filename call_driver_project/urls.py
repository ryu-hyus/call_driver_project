from django.contrib import admin
from django.urls import include, path
from calldriverapp.views.member_info import CustomerLoignView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('calldriverapp.urls.customer_urls')),
    path('center/', include('calldriverapp.urls.center_urls')),
    path('center/', include('calldriverapp.urls.center_urls')),
    path("", CustomerLoignView.as_view(), name="customer_login"),
]
