from django.db import models
from django.contrib.auth.models import User


class Blog(models.Model):
    users=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    description=models.TextField(max_length=500,null=True,blank=True)
    complete=models.BooleanField(default=False)
def __str__(self):
    return self.description
class Meta:
    ordering=['complete']