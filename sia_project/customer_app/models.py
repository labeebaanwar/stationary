from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class customer(models.Model):
    
    live=1
    delete=0
    delete_choice=((live,'live'),(delete,'delete'))
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    name=models.CharField(max_length=250)
    phone=models.IntegerField()
    address=models.TextField()
    user=models.OneToOneField(User,on_delete=models.SET_NULL, null=True, related_name='customer_profile')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    


