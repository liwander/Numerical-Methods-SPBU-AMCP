from input import borders
from scipy.integrate import quad as qd 

def integrand(wf, s):
    return lambda x : wf(x) * (x ** s)

def calculateSOrderMoment(weightFunction, order, borders):
    return qd(integrand(weightFunction, order), borders[0], borders[-1])

def calculateMoments(weightFunction, borders, num):
    moments = []
    
    for i in range(num):
        moments.append(calculateSOrderMoment(weightFunction, i, borders)[0])

    return tuple(moments)
