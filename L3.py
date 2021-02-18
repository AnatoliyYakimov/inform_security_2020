import numpy as np
from functools import reduce

basis = np.array([29, 31, 32])

M = reduce(lambda x, y: x * y, basis)

print("Allowed all values till {}".format(M))

def toModular(num):
    return np.array([num % basisElement for basisElement in basis])


def fromModular(num):
    for i in range(M):
        if (num == dictionary[i]).all():
            return i


def add(x, y):
    return fromModular((toModular(x) + toModular(y)) % basis)


def sub(x, y):
    return fromModular((toModular(x) - toModular(y)) % basis)

def mult(x, y):
    return fromModular(toModular(x) * toModular(y) % basis)

def mod(x):
    return fromModular(toModular(x) % basis)

def mod2(num):
    return np.array(list(map(lambda x: x / 2 if x % 2 == 0 else (x - 1) / 2, num)))

# def exp(x, y):
#     res = x
#     N = fromModular(y)
#     for i in range(N):
#         res = (res * x) % basis
#     return res
#     # if (y == 0).all():
#     #     return toModular(1)
#     # if (y % 2 == 0).all():
#     #     return exp((x * x) % basis, mod2(y))
#     # return (x * exp((x * x) % basis, mod2(y))) % basis

#Так и не смог реализовать деление для N-мерного базиса
def div(x, y):
    if x % y != 0:
        print("Can't div {} on {}".format(x, y))
        return None
    modX = toModular(x)
    modY = toModular(y)
    modYInv = exp(modY, basis)
    return fromModular((modX * modYInv) % basis)


dictionary = [toModular(i) for i in range(M)]

x = toModular(2)

print(x)

y = fromModular(x)

print(y)

res = add(24, 12)

print(res)

res = sub(20, 3)

print(res)

res = mult(5, 3)

print(res)

res = div(1872, 9)

print(res)