from flask import Flask, render_template
import mlab
from mongoengine import*
from models.service import Service

app = Flask(__name__)
mlab.connect()

# Desin pattern (MVC , MVP)
# # Design database
# class Service(Document) :
#     name = StringField()
#     yob = IntField()
#     gender = IntField()
#     height = IntField()
#     phone = StringField()
#     address = StringField()
#     status = BooleanField()

# new_service = Service(
#     name = "Hoàng Sơn",
#     yob = 1992,
#     gender = 1,
#     height =  175,
#     phone = "0987653321",
#     address ="Hà Nội",
#     status =False
# )

# new_service.save()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service  = Service.objects(gender = g,yob__lte = 1998,height__gte =165 )

    return render_template('search.html',all_service = all_service)

@app.route('/customer')    
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

if __name__ == '__main__':
  app.run(debug=True)
 