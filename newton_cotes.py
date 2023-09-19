from moments import calculateMoments

import numpy as np
from scipy.linalg import solve as slv


def findQFcoefs(wf, partition):
    borders = (partition[0], partition[-1])

    u = np.array(calculateMoments(wf, borders, len(partition)))
    m = createMatrix(partition)
    A = slv(m, u)
    return A
   
def createMatrix(partition):
    m = np.zeros((3, 3))
    for s in range(0, 3):
        for i in range(0, 3):
            m[s, i] = partition[i] ** s

    return m
      