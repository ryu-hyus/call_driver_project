import datetime
from django.db import models

class BaseModel(models.Model):
    is_deleted = models.BooleanField(default=False)

    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True)

    # objects = BaseCommonManager()

    class Meta:
        abstract = True
    
    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = datetime.datetime.now()
        self.save()