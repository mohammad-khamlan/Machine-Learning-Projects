from flask import Flask, request, jsonify
import pickle
import sklearn
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
    with open(str(path), 'rb') as f:
        model = pickle.load(f)
    return model



@app.route('/', methods=['GET', 'POST'])
def predict():
    """
    predict the house price by using the model
    :param: none
    :return: house price prediction
    """

    features = []

    if request.method == 'POST':
        #get features from json request
        req_json = request.json
        
        features.append(req_json['feature1'])
        features.append(req_json['feature2'])
        features.append(req_json['feature3'])
        features.append(req_json['feature4'])
        features.append(req_json['feature5'])
        features.append(req_json['feature6'])
        
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = str(model.predict(features))
        #return the result of the model
        return jsonify(result)

        
    else:
        #get features from get url
        
        features = request.args.get("feature1")
        features = request.args.get("feature2")
        features = request.args.get("feature3")
        features = request.args.get("feature4")
        features = request.args.get("feature5")
        features = request.args.get("feature6")
        
        #reshape the 1d array to 2d array to pass it to the model
        features = np.asarray(features, dtype=float).reshape(1,6)
        result = model.predict(features)
        #return the result of the model
        return str(result)    


if __name__ == '__main__':
    #Pass argument (path) from terminal
    parser = ArgumentParser()
    parser.add_argument('-p')
    args = parser.parse_args()
    path = args.p
    #Loaded model
    model = loaded_model() 
    #Run flask application
    app.run(debug=True)


