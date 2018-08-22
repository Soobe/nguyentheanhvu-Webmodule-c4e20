
from mongoengine import *

class Customer(Document):
    name = StringField()
    gender = IntField()
    phone = StringField()
    yob = StringField()
    company = StringField()
    contacted = BooleanField()