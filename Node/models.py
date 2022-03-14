from django.db import models
import uuid
# Create your models here.
class Node(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=70)
    current_status = models.BooleanField(default=False,null=True,blank=True)
    active = models.BooleanField(default=False)
    activate_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name