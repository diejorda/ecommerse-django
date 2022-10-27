from distutils.command.upload import upload
from email.policy import default
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
# Create your models here.

## create categories of items
CATEGORY_CHOICES=(
    ('S','Shirt'),
    ('SW','Sport wear'),
    ('OW', 'Out wear')
)
LABEL_CHOICES=(
    ('primary-color', 'p',),
    ('secondary-color', 's',),
    ( 'danger-color', 'd',)
)


### all items
class Item(models.Model):
    title= models.CharField(max_length=100)
    price= models.FloatField()
    img= models.ImageField(upload_to='items_img' ,default='imageNotFound.png')
    description= models.TextField()
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2, default='S')
    label=models.CharField(choices=LABEL_CHOICES, max_length=15, default='primary-color')
    
    

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
    

User_model= get_user_model()
class CUser(models.Model):
    user= models.ForeignKey(User_model, on_delete=models.CASCADE)
    address= models.CharField(max_length=30, blank=True , null=True)
    personal_id=models.IntegerField(blank=True, null=True)
    country=models.CharField(blank=True, max_length=20, null=True)
    state=models.CharField(blank=True, max_length=20, null=True)
    zipcode=models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.user.username
    