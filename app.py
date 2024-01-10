from flask import Flask, render_template, request
import pickle

app = Flask(__name__, template_folder='./templates',static_folder='./static')
model = pickle.load(open('model.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template("index.html", **locals())

@app.route("/predict", methods = ["POST", "GET"])
def predict():
    sepalLength = float(request.form["sepalLength"])
    sepalWidth = float(request.form["sepalWidth"])
    petalLength = float(request.form["petalLength"])
    petalWidth = float(request.form["petalWidth"])

    result = model.predict([[sepalLength, sepalWidth, petalLength, petalWidth]])[0]

    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug = True)