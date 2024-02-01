from django.db import models

from datetime import datetime


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    addres = models.CharField(max_length=200)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, ' \
               f'addres: {self.addres}, date_reg: {self.date_reg}'


class Product(models.Model):
    name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    product_added_date = models.DateTimeField(auto_now_add=True)





class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)        # клиент
    products = models.ManyToManyField(Product)                          # заказанный продукт
    total_price = models.DecimalField(max_digits=8, decimal_places=2)   # общая сумма заказа
    date_ordered = models.DateTimeField(auto_now_add=True)              # дата оформления заказа


    # def get_summary(self):
    #     total_price = self.content.split()
    #
    #     return f'{" ".join(words[:12])}...'
