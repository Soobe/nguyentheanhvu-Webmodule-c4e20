from mongoengine import*

class Account(Document):
    fullname = StringField()
    username = StringField()
    pasword = StringField()
    email = EmailField()