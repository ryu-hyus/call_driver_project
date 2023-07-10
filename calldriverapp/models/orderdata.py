from django.db import models
from .basemodels.basemodels import BaseModel
from .customer import Customer

# class OrderData(BaseModel):
#     customer = models.ForeignKey(Customer, related_name='order_customer', on_delete=models.CASCADE) 
#     start_address = models.CharField(max_length=255, default='')
#     end_address = models.CharField(max_length=255, default='')
#     order_kind = models.CharField(max_length=255, default='')
#     ordered_datetime = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.customer)