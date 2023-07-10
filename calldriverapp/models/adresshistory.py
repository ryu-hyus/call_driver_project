from django.db import models
from .customer import Customer
from .orderdata import OrderData
from .basemodels.basemodels import BaseModel

class AddressHistory(BaseModel):
    ADRESS_TYPE = (
        ('출발지'),
        ('목적지'),
    )

    customer = models.ForeignKey(Customer, related_name='history_customer', on_delete=models.CASCADE)
    raw_address = models.CharField(max_length=255, default='')
    adress_type = models.CharField(max_length=255, choices=ADRESS_TYPE)

    def __str__(self):
        return str(self.customer) 