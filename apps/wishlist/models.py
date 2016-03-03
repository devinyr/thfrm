from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    itemname = models.TextField(max_length=50)
    added_by = models.ForeignKey(User)    
    created_at = models.DateField(auto_now_add=True)
    class Meta:
        db_table = 'items'

class WishList(models.Model):
    uname = models.ManyToManyField(User)
    item_id = models.ManyToManyField(Item)
    class Meta:
        db_table = 'wishlists'
 