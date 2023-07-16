from datetime import date
from django.db import models
from .basemodels.basemodels import BaseModel

class OperationOnOff(BaseModel):
    operation_onoff = models.BooleanField(default=False)

    def set_off(self):
        self.operation_onoff = False

    def set_on(self):
        self.operation_onoff = True

    class Meta:
        app_label = "calldriverapp"
        db_table = "operation_onoff"

    def __str__(self):
        return str(self.operation_onoff) 

class OperationDay(BaseModel):
    operation_day = models.DateField(default = date.today())

    def set_day(self):
        self.operation_day = date.today()

    class Meta:
        app_label = "calldriverapp"
        db_table = "operation_day"

    def __str__(self):
        return str(self.operation_day) 