import numpy as np

c = 1 / 2
A, B, C = 2, -1, -1


a = c
b = np.array([1 - 1 / ( 2 * c) , 1 / ( 2 * c)])

vector = np.array

def f(x : float,y : vector)-> vector: 
    y1 =  2 * x * y[3] * y[1] ** (1 / B) 
    y2 =  2 * B * x * np.exp(( B / C ) * (y[2] - A)) * y[3] 
    y3 =  2 * C * x * y[3]
    y4 =  -2 * x * np.log(y[0])
    return np.array([y1, y2, y3, y4])

cauchy_conditions = np.array([0, 1, 1, A ,1])
segm = np.array([0, 5]) 

def answer(x: float) -> vector:
    y1 = np.exp(np.sin(np.power(x,2)))
    y2 = np.exp(-1 * np.sin(np.power(x,2)))
    y3 = C * np.sin(np.power(x,2)) + A
    y4 = np.cos(np.power(x,2))
    return np.array([y1, y2, y3, y4])