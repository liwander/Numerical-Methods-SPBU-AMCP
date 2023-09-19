
xn = [0.5, 1.35, 2.2]
xg = [0.729096893490137, 1.48158666223834, 2.12264977760485]

An = [0.14719745, 1.47197449, 1.47197449]
Ag = [0.44429685 ,1.003274  ,1.64357557]

def scalMul(v1, v2):
    sum = 0
    for i in range(len(v1)):
        sum += v1[i] * v2[i]
        
    return sum  

print(scalMul(xn, An))
print(scalMul(xg, Ag))
