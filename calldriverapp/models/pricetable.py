from django.db import models
from .basemodels.basemodels import BaseModel

class PriceTable(BaseModel):
    start_section = models.CharField(max_length=255, default='')
    end_section = models.CharField(max_length=255, default='')
    calculated_price = models.IntegerField(default=0)