from common import *
import matplotlib.pyplot as plt
from collections.abc import Callable


def getK(f, x, y, h, s, a, c):
    K = [None] * s
    for i in range(s):
        K[i] = f(x + c[i] * h, y + h * np.dot(a[i, :i], K[:i]))
    return np.array(K)


def runge(f: Callable[[float, vector], vector],
          cauchy_cond: vector,
          segment: vector,
          h: float,
          s: int, 
          a: np.ndarray,
          b: np.array,
          c: np.array
          ) -> None:
    
    n = int(np.ceil((segment[1] - segment[0]) / h))
    x, y = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])

    for i in range(n):
        K = getK(f, x[-1], y[-1], h, s, a, c)
        print(b.shape, K.shape)
        y = np.append(y,  [y[-1] + h * np.matmul(b, K)], axis=0)
        x = np.append(x,  x[-1] + h)

    plt.plot(x, y)

    t = np.arange(segment[0], segment[-1] + h, h)
    z = answer(t).transpose() + 5
    plt.plot(t, z)

    plt.savefig('./odesf.png')

def runge_kutta_method():
    runge(f, cauchy_conditions, segm, 1e-2, 3, a, b, c)