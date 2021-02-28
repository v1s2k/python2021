import math


def f5(x,y,z):
    d1 = (math.cos(z**7-y**2+40))-(x**8/88)
    d2 = math.sqrt((81*z**3-8*x**8-31)/(y**6/83+math.cos(y)))
    d3 = 50*(y**2)+90*y
    res=d1 - d2 - d3
    return ('%.2e' % res)


print(f5(1,30,9))
print(f5(2, 94, 64))