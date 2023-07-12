from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('calldriverapp.urls.customer_urls')),
    path('center/', include('calldriverapp.urls.center_urls')),

]
