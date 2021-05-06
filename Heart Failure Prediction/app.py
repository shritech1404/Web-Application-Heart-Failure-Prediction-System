from flask import Flask, request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)
model = pickle.load(open('heart.pkl', 'rb'))

@app.route('/')
def hello_world():
    return render_template("heart.html")

@app.route('/after',methods=['POST','GET'])
def after():
    features = [float(x) for x in request.form.values()]
    final = [np.array(features)]
    print(features)
    print(final)
    output = model.predict(final)


    if output==0:
        return render_template("main1.html")
    else:
        return render_template("main2.html")

if __name__ == '__main__':
    app.run(debug=True)