from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    published_date=models.DateField()
    isbn=models.CharField(max_length=13)
    price=models.DecimalField(decimal_places=2,max_digits=6)
   
    
