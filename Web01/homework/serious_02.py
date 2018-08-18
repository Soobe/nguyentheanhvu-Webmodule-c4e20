from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')

def index(username):

    users = {
        "Quy": {
            "name" : "Dinh Quy",
            "age" : 20,
            "sex": "male"
        },
        "TuanAnh" : {
            "name" : "Huynh Tuan Anh",
            "age" : 23,
            "sex": "male"
        },
        "Quan":{
            "name": "Nguyen Anh Quan",
            "age": 22,
            "sex": "male"
        }
    }
    
    if username in users:
        return render_template('user.html',username=users[username])

    else:
        return "User not found"
   
if __name__ == '__main__':
  app.run(debug=True)