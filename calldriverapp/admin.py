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


@admin.register(PriceFile)
class PriceFileAdmin(admin.ModelAdmin):
    list_display = ("id", "file", 'uploaded_at',)


class OperationDayAdmin(admin.ModelAdmin):
    list_display = ("id", "operation_day",)


# Register your models here.
admin.site.register(OperationOnOff)
admin.site.register(OperationDay, OperationDayAdmin)
admin.site.register(AddressHistory)
admin.site.register(OrderData)
admin.site.register(PriceTable, PriceAdmin)
admin.site.register(MyUser)
admin.site.register(PriceFile)

