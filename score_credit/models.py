from mongoengine import *


class IncomeSource(EmbeddedDocument):
    name = StringField()
    value = FloatField()


class Property(EmbeddedDocument):
    name = StringField()
    value = FloatField()


class Score(Document):
    cpf = IntField()
    age = IntField()
    address = StringField()
    city = StringField()
    state = StringField()
    income_source = ListField(EmbeddedDocumentField(IncomeSource))
    property = ListField(EmbeddedDocumentField(Property))


connect('scoredb')
