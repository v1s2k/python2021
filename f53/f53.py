import math
def third(n, m):
    a = 0
    b = 0
    for i in range (n):
        for j in range (m):
            a += math.cos(i) - 85*math.pow((i+1), 8)
            b += 15*math.pow((j+1), 4) + math.fmod(((i+1)**2), 27) 

    result = a - b
    return ('%.2e' % result)

print(third(84,100))
print(third(94,26))
