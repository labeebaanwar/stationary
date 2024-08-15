from django.db import models

# Create your models here.
class products(models.Model):
    
    live=1
    delete=0
    delete_choice=((live,'live'),(delete,'delete'))
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    title=models.CharField(max_length=250)
    price=models.FloatField()
    description=models.TextField()
    image=models.ImageField(upload_to='media/products')
    priority=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
    


