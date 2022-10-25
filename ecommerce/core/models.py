from email.policy import default
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings
# Create your models here.

### all items
class Item(models.Model):
    title= models.CharField(max_length=100)
    price= models.FloatField()
    description= models.TextField()
    color= models.CharField()

    def __str__(self):
        return self.title
    

### once selected is a order item
class OrderItem(models.Model):
    item= models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

### CART
class Order(models.Model): 
    user= models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    ordered = models.BooleanField(default=False)
    items= models.ManyToManyField(OrderItem)
    start_date= models.DateField(auto_now_add=True)
    ordered_date= models.DateField()


    def __str__(self):
        return self.user.username