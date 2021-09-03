from django.db import models
from django.utils import timezone

Status=[
("PENDING", "PENDING"),
("BOUGHT", "BOUGHT"),
("NOT AVAILABLE", "NOT AVAILABLE")
]

class Grocery(models.Model):
    Item_name = models.CharField(max_length=200)
    Item_quantity = models.IntegerField()
    Item_status = models.CharField(choices=Status, max_length=20)
    Date =models.DateTimeField(default=timezone.now)
