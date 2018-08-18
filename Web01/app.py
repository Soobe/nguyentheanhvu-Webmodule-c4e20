from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    posts = [
    {    
        "title": "Thơ con ếch",
        "content":"Nội dung bài thơ",
        "author":"Vũ Anh Nguyễn",
        "author_sex": 1
    },
    {
         
        "title": "Từ Từ",
        "content":"Từ Từ",
        "author":"Thu Minh",
        "author_sex": 2
    },
    {
         
        "title": "Đen Vãi",
        "content":"Đen",
        "author":"Đặng Hải",
        "author_sex": 1
    },
]
    # return "<h1>Hello C4E20</h1>"
    return render_template('index.html', posts = posts)

@app.route('/Hello')
def say_hello():
    return"Hello from the other side"

@app.route('/Say-hi/<name>/<age>')
def say_hi(name, age):
    return"Hi {}, you're {} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x , y):
    return str(x + y)

if __name__ == '__main__':
  app.run(debug=True)
 