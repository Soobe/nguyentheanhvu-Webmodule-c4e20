import mongoengine

# mongodb://admin:admin123@dbh54.mlab.com:27547/cms-app-c4e20

host = "dbh54.mlab.com"
port = 27547
db_name = "cms-app-c4e20"
user_name = "admin"
password = "admin123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)


