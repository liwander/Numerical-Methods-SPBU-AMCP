a = 1.5
b = 2.3
alpha = 1/5
betta = 0

def weightFunc(x):
    return ((x - a) ** -alpha) * ((b - x) ** -betta)


x1 = a
x2 = (a + b) / 2
x3 = b
xs = (x1, x2, x3)

gaussGFPointsNumber = 3
borders = (a, b)