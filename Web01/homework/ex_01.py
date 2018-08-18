from flask import Flask , render_template ,redirect

app = Flask(__name__)

@app.route('/')
def hello():
    return"HELLO C4E20"

@app.route('/aboutme')   
def index01():
    post ={
        "name" : "Anh Vũ",
        "age" : 20,
        "school" : "Công nghệ GTVT",
        "favorite":"girl "
        }

    return render_template('index01.html', post = post)

@app.route('/school')
def fun():
    return redirect("https://techkids.vn/", code=302)

if __name__ == '__main__':
    app.run(debug=True)    

