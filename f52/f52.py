import math


def f12(x):
    if (x <= 88):
        return (math.cos(x**7-x**2+40))-(x**3/88)
    elif ((88 <= x) and (x < 137)):
        return 81*x**3-8*x**8-31
    elif ((137 <= x) and (x <219)):
        return (((x**4+(x**5/67))**6)/37)+95*x**8
    elif ((219 <= x) and (x <291)):
        return math.tan(x**5)+x**6-21
    elif (291 <= x):
        resf= 82*((x**5-math.exp(x))**4)-32*x**5
        return ('%.2e' % resf)
print(f12(137))