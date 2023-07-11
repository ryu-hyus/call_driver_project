from django.contrib import admin
from calldriverapp.models.adresshistory import AddressHistory

from calldriverapp.models.operation import OperationDay, OperationOnOff
from calldriverapp.models.orderdata import OrderData
from calldriverapp.models.pricetable import PriceTable

# Register your models here.
admin.site.register(OperationOnOff)
admin.site.register(OperationDay)
admin.site.register(AddressHistory)
admin.site.register(OrderData)
admin.site.register(PriceTable)
