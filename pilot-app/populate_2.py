
from models.service import Service
import mlab
from faker import Faker
from random import randint ,choice
mlab.connect()

fake = Faker()

for i in range(50):
    print('Saving customer', 1 + i,".......")
    new_customer = Customer(

    name = fake.name(),
    yob = randint(1996, 2000),
    gender = randint(0,1),
    height = randint(150,190),
    phone = fake.phone_number(),
    company= fake.company(),
    contacted= choice([True, False]

    )

new_customer.save()
