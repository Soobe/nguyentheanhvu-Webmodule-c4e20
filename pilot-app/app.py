from flask import Flask, render_template
import mlab
from mongoengine import*
from models.service import Service
from models.customer import Customer

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
    all_customers = Customer.objects()
    return render_template('customer.html', all_customer = all_customer)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service= all_service)    

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        # return "Deleted"
        return redirect(url_for('admin'))
    else:
        return "Service Not Found"    

@app.route('/detail/<service_id>')
def detail(service_id):
    service = Service.objects.with_id(service_id)
    return render_template('detail.html', service = service)    

@app.route('/newservice', methods = ['GET', 'POST'])
def create():
    if request.method == 'GET':
        return render_template('newservice_hw.html')

    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']

        new_service = Service(
            name = name,
            yob = yob,
            phone = phone,
            gender = gender
        )
        new_service.save()

        return redirect(url_for('admin'))   

@app.route('/updateservice/<service_id>', methods = ['GET', 'POST'])
def update_service(service_id):
    service = Service.objects.with_id(service_id)
    if request.method == 'GET':

        return render_template('updateservice_hw.html', service = service)

    elif request.method == 'POST':
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']

        service.name = name
        service.yob = yob
        service.phone = phone
    
        service.save()
        
        return redirect(url_for('admin'))
   

if __name__ == '__main__':
  app.run(debug=True)
 