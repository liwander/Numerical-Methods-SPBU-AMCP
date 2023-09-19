a = 0.5
b = 2.2
alpha = 0
betta = 3/5

def weightFunc(x):
    return ((x - a) ** -alpha) * ((b - x) ** -betta)


x1 = a
x2 = (a + b) / 2
x3 = b
xs = (x1, x2, x3)

gaussGFPointsNumber = 3
borders = (a, b)