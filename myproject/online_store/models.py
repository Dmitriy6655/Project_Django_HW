import django
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    date_reg = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, phone: {self.phone}, ' \
               f'address: {self.address}, date_reg: {self.date_reg}'


class Goods(models.Model):
    name = models.CharField(max_length=100)
    product_description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity_product = models.IntegerField()
    image = models.ImageField(upload_to='goods/')
    product_added_date = models.DateTimeField(auto_now_add=True)

    # def total_price(self):
    #     return self.price * self.quantity_product
    def __str__(self):
        return f'name product: {self.name}, product_description: {self.product_description}, price: {self.price}, ' \
               f'quantity_product: {self.quantity_product}, product_added_date: {self.product_added_date}'



class Order(models.Model):
    customer = models.ForeignKey(Client, on_delete=models.CASCADE)          # клиент
    products = models.ManyToManyField(Goods)                                # заказанный продукт
    total_price = models.DecimalField(max_digits=8, decimal_places=2)       # общая сумма заказа
    date_ordered = models.DateTimeField(auto_now_add=True)                  # дата оформления заказа

    def __str__(self):
        return f'customer: {self.customer}, products: {self.products}, total_price: {self.total_price}, ' \
               f'date_ordered: {self.date_ordered}'




class Image(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    image = models.ImageField(upload_to='images/', null=True, max_length=255)

    def __repr__(self):
        return 'Image(%s, %s)' % (self.title, self.image)

    def __str__(self):
        return self.title
