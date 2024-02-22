from django.core.management.base import BaseCommand
from online_store.models import Client, Goods, Order
from faker import Faker

# from _decimal import ROUND_DOWN
from django.core.management.base import BaseCommand
# from faker import Faker
from decimal import Decimal




class Command(BaseCommand):
    help = "Create new order"

    def add_arguments(self, parser):
        # faker = Faker(locale='ru-ru')
        parser.add_argument('--client_id', default=6, type=int, help='Client ID')
        parser.add_argument('--goods_id', default=6, type=int, help='Goods ID')
        parser.add_argument('--amount', default=6, type=int, help='Count of goods in order')

    def handle(self, *args, **kwargs):
        customer_pk = kwargs.get('client_id')
        goods_pk = kwargs.get('goods_id')
        amount = Decimal(kwargs.get('amount'))
        client = Client.objects.filter(pk=customer_pk).first()
        goods = Goods.objects.filter(pk=goods_pk).first()
        total_price = self.__total_price(goods, amount)



        # print(f"customer_pk={customer_pk}")
        # print(f"goods_pk={goods_pk}")
        # print(f"amount={amount}")
        # print(f"client={client}")
        # print(f"goods={goods}")
        # print(f"total_price={total_price}")

        # order1 = Order.objects.get(pk=3)


        new_order = Order.objects.create(
            customer=client,
            total_price=0,
            # products=,
            date_ordered=''
        )

        # Order.objects.get(products=goods1).products.add()





        self.stdout.write(f'Order {new_order.pk} created,  Total price {total_price}')

    @staticmethod
    def __total_price(goods, amount):
        total = goods.price * amount
        return total
