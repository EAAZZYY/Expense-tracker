from django.db import models

# Create your models here.

categories = [
    ("Data","Data"),
    ("Personal","Personal"),
    ("Food","Food"),
    ("Pleasure","Pleasure"),
    ("Business","Business"),
    ("Gift","Gift"),
]

class MyExpense(models.Model):
    bought = models.CharField(max_length=200)
    amount = models.IntegerField()
    category = models.CharField(max_length=100,choices=categories)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.bought