from django.db import models

from .operation import OperationDay
from .basemodels.basemodels import BaseModel
from .customer import MyUser
from datetime import date

class OrderData(BaseModel):
    ORDER_KIND = (
        ('order','주문'),
        ('change','변경'),
        ('cancel','취소')
        )
    
    customer = models.ForeignKey(MyUser, related_name='order_customer', on_delete=models.CASCADE, default='') 
    start_address = models.CharField(max_length=255, default='')
    end_address = models.CharField(max_length=255, default='')
    order_kind = models.CharField(max_length=255, choices= ORDER_KIND, default='주문')
    operation_day = models.DateField(default= date.today())
    order_type = models.BooleanField(default=True)
    is_hide = models.BooleanField(default=False)

    def OrderConfirm(self):
        self.order_type = False

    def OrderHide(self):
        self.is_hide = True


    class Meta:
        app_label = "calldriverapp"
        db_table = "orderdata"

    def __str__(self):
        return str(self.start_address)