import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import math
import matplotlib.pyplot as plt


def trained_model():
    data = pd.read_csv('test.csv')
    model = LinearRegression()
    model.fit(data[['math']], data.cs)
    return model.coef_, model.intercept_


def gradient_descent(x, y):

    m = 0
    b = 0

    iterations = 1000000
    n = len(x)
    learning_rate = 0.08
    cost_previous = 0

    

    for i in range(iterations):

        y_i = m*x + b
        cost = (1/n)*sum([value**2 for value in (y-y_i)])
        

        md = -(2/n)*sum(x*(y-y_i))
        bd = -(2/n)*sum(y-y_i)

        m = m - learning_rate*md
        b = b - learning_rate*bd

        if math.isclose(cost, cost_previous, rel_tol=1e-20):
            break
        cost_previous = cost
        print("m = {}, b = {}, cost = {}, iteration = {}".format(m, b, cost, i))

    return m, b



if __name__ == "__main__" :

    df = pd.read_csv('test.csv')

    x = np.array(df.math)
    y = np.array(df.cs)

    plt.scatter(x,y,color='red',marker='+',linewidth='5')
    plt.plot(x,color='green')

    m, b = gradient_descent(x, y)
    print("Using gradient descent function: Coef = {}, Intercept = {}".format(m, b))
    

    m_model, b_model = trained_model()
    print("Using sklearn model: Coef = {}, Intercept = {}".format(m_model, b_model))







