from django.db import models
from .customer import MyUser
from .basemodels.basemodels import BaseModel

class AddressHistory(BaseModel):
    ADDRESS_TYPE = (
        ('start' , '출발지'),
        ('end', '목적지')
        )

    customer = models.ForeignKey(MyUser, related_name='history_customer', on_delete=models.CASCADE, default='')
    raw_address = models.CharField(max_length=255, default='')
    adress_type = models.CharField(max_length=255, choices = ADDRESS_TYPE)

    class Meta:
        app_label = "calldriverapp"
        db_table = "addrees history"

    def __str__(self):
        return str(self.raw_address)