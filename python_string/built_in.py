# coding: utf-8

x = 'Hello, world!'
print(len(x))
print(max(x))
print(min(x))
print(list(zip(x, x)))
print(sorted(x))
print(list(reversed(x)))
print(list(enumerate(x)))


def add(a, b):
    return a + b


print(list(map(add, x, x)))


print(eval('3+4'))
c, d = 3, 5
print(eval('c+d'))
