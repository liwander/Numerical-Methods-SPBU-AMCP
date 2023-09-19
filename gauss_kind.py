from moments import calculateMoments
from scipy.linalg import solve as slv
from sympy.solvers import solve
from sympy import Symbol, re, im
from math import pow

import numpy as np

def findNodalPolynomialCoefficents(moments):
    n = int(len(moments) / 2)
    b = []

    a = np.ndarray((n , n))
    for s in range(n):
        for i in range(n):  
            a[s, i] = moments[i + s]

        b.append(-1 * moments[n + s])

    NPCoefs = slv(a, np.array(b))
    return NPCoefs


def findPartition(coefs, deg):
    x = Symbol('x')
    equation = [x ** deg]
    for i in range(deg):
        equation.append(coefs[i] * x ** (deg - i - 1))

    return solve(x ** deg + coefs[2] * x** 2+ coefs[1] * x + coefs[0], x)


def findGaussKindQFCoefficents(wf, borders, nodeNum):
    moments = calculateMoments(wf, borders, 2 * nodeNum)

    NPCoefs = findNodalPolynomialCoefficents(moments)

    nodes = findPartition(NPCoefs, nodeNum)

    nodes = [re(nd) for nd in nodes if im(nd) < 1e-10]

    matrQFCoefs = np.ndarray((nodeNum, nodeNum))
    b = []
    for s in range(nodeNum):
        for i in range(nodeNum):  
            matrQFCoefs[s, i] = pow(nodes[i], s)

        b.append(moments[s])

    QFcoefs = slv(matrQFCoefs, np.array(b))
    return QFcoefs