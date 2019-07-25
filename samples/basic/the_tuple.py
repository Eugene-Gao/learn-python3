#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ('Michael', 'Bob', 'Tracy')
print('classmates =', classmates)
print('len(classmates) =', len(classmates))
print('classmates[0] =', classmates[0])
print('classmates[1] =', classmates[1])
print('classmates[2] =', classmates[2])
print('classmates[-1] =', classmates[-1])

# cannot modify tuple:
classmates[0] = 'Adam'
# -----------------------------------------------
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印 Apple:
print(L[0][0])
# 打印 Python:
print(L[1][1])
# 打印 Lisa:
print(L[2][2])
