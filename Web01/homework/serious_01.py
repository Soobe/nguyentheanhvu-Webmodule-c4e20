from flask import Flask , render_template

app = Flask(__name__)

@app.route('/bmi,/<int:weight>,/<int:height>')

def bmi(weight,height):
    bmi = weight / ((height/100)**2)

    if bmi < 16:
        return "Severely underweight"

    elif bmi < 18.5:
        return "underweight"

    elif bmi < 25:
        return "normal"

    elif bmi  < 30:
        return "Overweight"

    elif bmi > 30:
        return "Obese"    

#using render_template :
body = {}

@app.route('/bmi1/<int:weight1>/<int:height1>')

def bmi1(weight1, height1):

    bmi1 = weight1 / ((height1/100)**2) 

    body['w'] = weight1

    body['h'] = height1

    body['bmi'] = bmi1

    return render_template('bmi.html', body = body)

if __name__ == '__main__': 
  app.run(debug=True)         