from models.service import Service
import mlab
from faker import Faker
from random import *

mlab.connect()

fake = Faker()

for i in range(40):
    print('Saving Service', i+1, '......')
    sex = randint(0, 1)

    if sex == 1:
        new_service = Service(
            name = fake.name(),
            yob = randint(1996, 2000),
            gender = sex,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice(['Buồn', 'Vui']),
            image = 'static/image/' + choice(['male.jpg','male-profile.jpg']),
            description = sample(['thích âm nhạc', 'thích chơi game', 'chơi guitar','thích gái', 'thích chơi piano'], 4),
            measurements = [randint(55,90),randint(55,90),randint(55,90)]
        )
    elif sex == 0:
        new_service = Service(
            name = fake.name(),
            yob = randint(1996, 2000),
            gender = sex,
            height = randint(150, 190),
            phone = fake.phone_number(),
            address = fake.address(),
            status = choice(['Buồn', 'Vui']),
            image = 'static/image/' + choice(['female.jpg','female-profile.jpg']),
            description = sample(['Thích trai', 'thích xoạc', 'thích âm nhạc', 'thích shopping', 'thích du lịch','Thích đọc sách' ], 4),
            measurements = [randint(55,90),randint(55,90),randint(55,90)]
        )        

    new_service.save()