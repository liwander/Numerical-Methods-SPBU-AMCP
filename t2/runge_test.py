from common import *
import matplotlib.pyplot as plt
from collections.abc import Callable


def getK(f, x, y, h):
    K = [f(x, y)]
    K.append(f(x + c * h, y + h * a * K[0]))
    return np.array(K)


def runge(f: Callable[[float, vector], vector],
          cauchy_cond: vector,
          segment: vector,
          h: float) -> None:
    n = int(np.ceil((segment[1] - segment[0]) / h))
    x, y = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])

    for i in range(n):
        # print(x[-1], y[-1])
        K = getK(f, x[-1], y[-1], h)
        y = np.append(y,  [y[-1] + h * np.dot(b, K)], axis=0)
        x = np.append(x,  x[-1] + h)

    plt.plot(x, y)

    t = np.arange(segment[0], segment[-1] + h, h)
    z = answer(t).transpose() + 5
    plt.plot(t, z)

    plt.savefig('./odesf.png')

def runge_kutta_method():
    runge(f, cauchy_conditions, segm, 1e-2)