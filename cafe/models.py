from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Menu(models.Model) :
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name

class Order(models.Model) :
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now=True)
    menu_count = models.IntegerField()
    order_price = models.IntegerField()

    def __int__(self):
        return self.menu_count
