from common import *
import matplotlib.pyplot as plt
from collections.abc import Callable

def local_margin(y, y2, p):
    return [np.array([(y - y2) * 1 / (1 - np.exp2(-p))])
            , np.array([(y - y2) * (1 / (np.exp2(p) - 1))])]

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
          p: int,
          a: np.ndarray,
          b: np.array,
          c: np.array,
          png_name: str = 'runge method'
          ) -> None:
    
    n = int(np.ceil((segment[1] - segment[0]) / h))
    x, y = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])
    x2, y2 = np.array([cauchy_cond[0]]), np.array([cauchy_cond[1:]])
    r2, r = local_margin(y[-1], y2[-1], p)
    # r = np.array()


    for i in range(n):
        K = getK(f, x[-1], y[-1], h, s, a, c)
        y = np.append(y,  [y[-1] + h * np.matmul(b, K)], axis=0)
        x = np.append(x,  x[-1] + h)

        if i % 2 == 0:
            K2 = getK(f, x2[-1], y2[-1], 2 * h, s, a, c)
            y2 = np.append(y2,  [y2[-1] + 2 * h * np.matmul(b, K2)], axis=0)
            x2 = np.append(x2,  x2[-1] + 2 * h)
        else:
            rx = local_margin(y[-1], y2[-1], p)
            r2 = np.append(r, rx[1], axis=0)
            r = np.append(r, rx[0], axis=0)



    fig, axs = plt.subplots(4)
    fig.suptitle(f'runge-kutta {s}-step {p}-order method')
    fig.tight_layout()
    axs[0].set_title('half step method')
    axs[0].plot(x, y)
    axs[1].set_title('half step mehtod error margin')
    axs[1].plot(x2, r)
    axs[2].set_title('normal step method')
    axs[2].plot(x2, y2)
    axs[3].set_title('normal step method error margin')
    axs[3].plot(x2, r2)

    plt.savefig(f'{png_name}')

    # t = np.arange(segment[0], segment[-1] + h, h)
    # z = answer(t).transpose() + 5
    # plt.plot(t, z)

    # plt.savefig('main_margin.png')

def runge_kutta_method(a, b, c, png_name):
    runge(f, cauchy_conditions, segm, (1e-2) / 2, len(b), len(b), a, b, c, png_name)