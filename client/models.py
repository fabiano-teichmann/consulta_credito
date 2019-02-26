from mongoengine import *


class Item(EmbeddedDocument):

    lender = StringField()
    value = FloatField()
    date_debt = DateTimeField()


class Client(Document):
    cpf = IntField()
    name = StringField()
    address = StringField()
    city = StringField()
    state = StringField()
    debt_list = ListField(EmbeddedDocumentField(Item))
    create_at = DateTimeField()



