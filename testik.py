#!/bin/python3
def parameters(n):
    res = []
    m = 2
    while n > 1:
        if n % m == 0:
            n = n // m
            res.append(m)
        else:
            m += 1
    return res
k = int(input("Введите число"))
print(parameters(k))



