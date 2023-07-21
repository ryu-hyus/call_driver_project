from django.contrib import admin

from calldriverapp.models import PriceFile
from calldriverapp.models.addresshistory import AddressHistory
from calldriverapp.models.customer import MyUser

from calldriverapp.models.operation import OperationDay, OperationOnOff
from calldriverapp.models.orderdata import OrderData
from calldriverapp.models.pricefile import PriceFile
from calldriverapp.models.pricetable import PriceTable


class PriceAdmin(admin.ModelAdmin):
    list_display = ("id", "start_section", "end_section", "calculated_price",)


class PriceFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", 'uploaded_at',)

class OperationDayAdmin(admin.ModelAdmin):
    list_display = ("id", "operation_day", "updated_at")

class OrderDataAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_id" ,"start_address","end_address","order_kind","order_type","is_hide","operation_day",)

class AddressHistoryAdmin(admin.ModelAdmin):
    list_display = ("id", "customer_id" ,"raw_address","trans_address","section_name","address_type",)

class MyUserAdmin(admin.ModelAdmin):
    list_display = ("id", "username" ,"name","phone_number","gear_type","is_staff","is_superuser",)

class OperationOnOffAdmin(admin.ModelAdmin):
    list_display = ("id", "operation_onoff" ,"created_at",)

# Register your models here.
admin.site.register(OperationOnOff, OperationOnOffAdmin)
admin.site.register(OperationDay, OperationDayAdmin)
admin.site.register(AddressHistory, AddressHistoryAdmin)
admin.site.register(OrderData, OrderDataAdmin)
admin.site.register(PriceTable, PriceAdmin)
admin.site.register(MyUser,MyUserAdmin)
admin.site.register(PriceFile, PriceFileAdmin)

