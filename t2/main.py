from runge import runge_kutta_method
import numpy as np


a = np.array([[0 , 0], [ 1 / 2, 0], [-1, 2]])
b = np.array([1 / 6, 2 / 3, 1 / 6])
c = np.array([0, 1 / 2, 1])

runge_kutta_method(a, b, c, png_name='odessa.png')


a = np.array([[ 0 ] , [1 / 2]])
b = np.array([ 0 , 1 ])
c = np.array([0, 1 / 2])

runge_kutta_method(a, b, c, png_name='kyiv.png')