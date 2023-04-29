import numpy as np
import matplotlib.pyplot as plt
import sklearn as scp
import tensorflow as tf

def gradientDescent(x,y,w,b,alpha,N):
    
    dJdw = 0
    dJdb = 0

    for xi,yi in zip(x,y):

        dJdw += -2*xi*(yi - (w*xi + b))
        dJdb += -2*(yi - (w*xi + b))

    w -= alpha*dJdw/N
    b -= alpha*dJdb/N      

    return w, b

def predict(epochs):
     
     w = 0
     b = 0

     for i in range(epochs):

        w,b = gradientDescent(x,y,w,b,alpha,m)
        yhat = w*x +b
        J = np.divide(np.sum((y-yhat)**2, axis=0), m)
        print(f'{epochs} loss is {J}, parameters w:{w}, b:{b}')

def LSM(x,y,N):

    sum_xy = 0
    sum_x = 0
    sum_y = 0
    sum_x2 = 0

    for xi,yi in zip(x,y):
        
        sum_xy += xi*yi
        sum_x += xi
        sum_y += yi
        sum_x2 += xi**2
    
    m = (N*sum_xy - sum_x*sum_y)/(N*sum_x2 - sum_x**2)
    b = (sum_y - m*sum_x)/N

    return m, b

def plott(x,y):

    plt.scatter(x,y)
    plt.xlabel('x')
    plt.xlabel('y')

if __name__ == "__main__":

    w = 0
    b = 0
    alpha = 0.1

    x = np.random.randn(10,1)
    y = 3*x + np.random.randn()
    N = x.shape[0]
    epochs = 50

    predict(epochs)