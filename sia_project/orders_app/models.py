from django.db import models
from customer_app.models import customer
from products_app.models import products

# Create your models here.
class order(models.Model):
    live=1
    delete=0
    cart_stage=1
    order_confirmed=1
    order_processed=2
    order_rejected=3
    order_delivered=4
    status_choice=((order_processed,'ORDER PROCESSED'),
                   (order_delivered,'ORDER DELIVERED'),
                   (order_rejected,'ORDER REJECTED'))
    order_status=models.IntegerField(choices=status_choice,default=cart_stage)

    delete_choice=((live,'live'),(delete,'delete'))
    delete_status=models.IntegerField(choices=delete_choice,default=live)
    owner=models.ForeignKey(customer,on_delete=models.SET_NULL,null=True,related_name='orders')
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)



class order_items(models.Model):
    product=models.ForeignKey(products,related_name='added_carts',on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField(default=1)
    owner=models.ForeignKey(order,on_delete=models.CASCADE,related_name='added_items')