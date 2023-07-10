from django.db import models
from .basemodels.basemodels import BaseModel

# class Customer(BaseModel):
#     # user_id = models.ForeignKey("AddressHistory", max_length=15, default='', related_name="addresshistory", on_delete=models.CASCADE)
#     user_password = models.CharField(max_length=255, default='')
#     phone_no = models.CharField(max_length=255, default='')
#     name = models.CharField(max_length=255, default='')
#     gear = models.CharField(max_length=255, default='')
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return str(self.name)