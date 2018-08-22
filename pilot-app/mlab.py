import mongoengine

# mongodb://<admin>:<admin123>@ds225902.mlab.com:25902/muadongkhonglanh-c4e20

host = "ds225902.mlab.com"
port = 25902
db_name = "muadongkhonglanh-c4e20"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


