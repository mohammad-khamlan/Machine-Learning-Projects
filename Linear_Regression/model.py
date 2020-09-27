import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pickle

data = pd.read_excel("data.xls")

x_train = data['X']
y_train = data['Y']

plt.scatter(x_train, y_train)
plt.show()

theta0 = 0
theta1 = 0
alpha = 0.0001
times = 10000
n = float(len(x_train))

for i in range(times): 
    y_pred = theta0 + theta1 * x_train
    theta0 = theta0 - alpha * (1/n) * sum(y_pred - y_train)
    theta1 = theta1 - alpha * (1/n) * sum(x_train * (y_pred - y_train))
print("theta0 = " + str(theta0), "theta1 = " + str(theta1))

y_pred = theta0 + theta1 * x_train

plt.scatter(x_train, y_train) 
plt.plot([min(x_train), max(x_train)], [min(y_pred), max(y_pred)], color='red')  # regression line
plt.show()

file = open("thetas.txt","w+")
file.write(str(theta0))
file.write(",")
file.write(str(theta1))
file.close()