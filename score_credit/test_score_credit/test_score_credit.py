from random import randint
from unittest import TestCase
from faker import Faker


from client.models import Client
from score_credit.models import Score, Property, IncomeSource


class TestScore(TestCase):
    def setUp(self):
        self.fake = Faker()
        self.clients = Client.objects.all()

    def test_save_score(self):
        for c in self.clients:
            score = Score(cpf=randint(1, 100))
            score.age = randint(12, 100)
            score.address = self.fake.address()
            score.city = self.fake.city()
            score.state = self.fake.state()
            property = Property(name=self.fake.company(), value=float(randint(1, 100000)))
            score.property.append(property)
            rent = IncomeSource(name=self.fake.company(), value=float(randint(1, 100000)))
            score.income_source.append(rent)
            self.assertIsInstance(score.save(), Score)
