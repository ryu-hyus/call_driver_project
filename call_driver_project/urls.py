from django.contrib import admin
from django.urls import include, path
from calldriverapp.views.customer import HomeTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('customer/', include('calldriverapp.urls.customer_urls')),
    path('center/', include('calldriverapp.urls.center_urls')),
    path('center/', include('calldriverapp.urls.center_urls')),
    path("", HomeTemplateView.as_view(), name="main_page"),
]
