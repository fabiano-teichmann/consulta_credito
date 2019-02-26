from datetime import timedelta, datetime
from unittest import TestCase
from faker import Faker
from random import randint
import mongoengine

from client.models import Client, Item


class TestModel(TestCase):
    def setUp(self):
        self.conn = mongoengine.connect('client')
        self.fake = Faker()

    def test_insert_database(self):
        for i in range(0, 100):
            client = Client(name=self.fake.name())
            client.cpf = randint(00000000000, 99999999999)
            client.address = self.fake.address()
            client.city = self.fake.city()
            client.state = self.fake.state()
            date_debt = datetime.now() - timedelta(days=randint(0, 1000))
            item = Item(lender=self.fake.company(), value=float(randint(1, 10000)), date_debt=date_debt)
            client.debt_list.append(item)
            self.assertIsInstance(client.save(), Client)


    def test_connect_database(self):
        Client.objects.first()
