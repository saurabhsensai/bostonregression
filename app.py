
from distutils.log import debug
import pickle
from typing import final
from unicodedata import name  
from flask import Flask, request,app,jsonify,url_for,render_template
import numpy as np
import pandas as pd 


app = Flask(__name__)
#load the model
<<<<<<< HEAD
regmodel = pickle.load(open("regmodel.pkl",'rb'))
=======
regmodel = pickle.load(open("regmodl.pkl"))
>>>>>>> 511d551188fe30162789cd98b19571541a4261ab
scalar = pickle.load(open("scaling.pkl",'rb'))


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api',methods=['POST'])
def predict_api():
    data =request.json['data']
    
    #the data we get is in the form of dictionary 
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=  scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regmodel.predict(new_data)
    print(output[0])
    
@app.route('/predict_api',methods=['POST'])
def predict_api():
    data=request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data=scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output=regmodel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

@app.route('/predict',methods=['POST'])
def predict():
    data =[float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).shape(1,-1))
    output = regmodel.predict(final_input)[0] 
    return render_template("home.html",prediction_text ="The house price is {}".format(output) )
    
    
    
    
if __name__=="__main__":
    app.run(debug=True)


