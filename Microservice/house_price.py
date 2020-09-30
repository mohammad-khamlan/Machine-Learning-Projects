  from flask import Flask, render_template, request, jsonify
import csv
import pickle
import numpy as np
from argparse import ArgumentParser

app = Flask(__name__)


def loaded_model():
    """
    loaded the model using path passed in the console
    :param: none
    :return: the model loaded from pickle file
    """
    #Loaded model by pickle packege
    with open(str(foo), 'rb') as f:
        model = pickle.load(f)
    return model



@app.route('/', methods=['GET', 'POST'])
def predict():
    """
    predict the house price by using the model
    :param: none
    :return: house price prediction
    """
    if request.method == 'POST':
        #get features from json request
        req_json = request.json
        for i in range(6):
            features.append(req_json['feature'])
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = str(model.predict(features))
        #return the result of the model
        return jsonify(result)

        
    else:
        #get features from get url
        features = request.args.getlist("feature")
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = model.predict(features)
        #return the result of the model
        return str(result)    


if __name__ == '__main__':
    #Pass argument (path) from terminal
    parser = ArgumentParser()
    parser.add_argument('-a')
    args = parser.parse_args()
    foo = args.a
    #Loaded model
    model = loaded_model() 
    #Run flask application
    app.run(debug=True)

