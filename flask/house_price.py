from flask import Flask, render_template, request
import csv

app = Flask(__name__)


def readcsv():
    thetas = []
    #read the thetas from csv file
    with open('param.csv', 'r') as file:
        thetas = list(csv.reader(file))
    return thetas



@app.route('/')
def start():
    return render_template('house_price.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # read features from user input
        features = []
        for i in range(1,7):
            features.append(request.form[str(i)])
        #Compute the price of the house
        price = float(thetas[1][0])
        for i in range(0,6):
            price += float(thetas[0][i]) * float(features[i]) 
        return "house price of unit area: " + str(price)
    
    else:
        return render_template('house_price.html')
    

if __name__ == '__main__':
    thetas = readcsv()
    app.run(debug=True)