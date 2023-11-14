from common import *
import matplotlib.pyplot as plt
from collections.abc import Callable


def getK(f, x, y, h):
    K = [f(x, y)]
    K.append(f(x + c * h, y + h * a * K[0]))
    return np.array(K)

def local_margin(y, y2):
    return np.array([(y - y2) * 1 / (1 - np.exp2(-2)), (y - y2) * (1 / (np.exp2(2) - 1))])

def runge(f: Callable[[float, vector], vector],
          cauchy_cond: vector,
          segment: vector,
          h: float) -> None:
    
    n = int(np.ceil((segment[1] - segment[0]) / h))
    x, y = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])
    x2, y2 = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])
    r = local_margin(y[-1], y2[-1])

    for i in range(n):
        # print(x[-1], y[-1])

        K = getK(f, x[-1], y[-1], h)
        y = np.append(y,  [y[-1] + h * np.dot(b, K)], axis=0)
        x = np.append(x,  x[-1] + h)

        if i % 2 == 0:
            K2 = getK(f, x2[-1], y2[-1], 2 * h)
            y2 = np.append(y2,  [y2[-1] + 2 * h * np.dot(b, K2)], axis=0)
            x2 = np.append(x2,  x2[-1] + 2 * h)
        else:
            r = np.append(r, local_margin(y[-1], y2[-1]), axis=0)


    print(r)
    # print(x, len(x), x2, len(x2), sep='\n')
    
    plt.plot(x2, y2)

    plt.plot(x, y + 10)

    t = np.arange(segment[0], segment[-1] + h, h)
    z = answer(t).transpose() + 5
    plt.plot(t, z)

    plt.savefig('./odesf.png')

def runge_kutta_method():
    runge(f, cauchy_conditions, segm, 1e-2)