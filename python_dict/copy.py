# coding: utf-8
import copy

fruits = {
    'apple': 30,
    'banana': 50,
    'pear': 200
}

real_fruits = fruits.copy()
print(real_fruits)

real_fruits['orange'] = 50
real_fruits.update({'cherry': 100})

print(real_fruits)
real_fruits['apple'] = real_fruits['apple'] - 5
print(real_fruits)
real_fruits['pear'] -= 3
print(real_fruits)

real_fruits.clear()
print(real_fruits)
print('第二天...')
real_fruits = fruits.copy()
print(real_fruits)

a = {1: [1, 2, 3]}
c = copy.deepcopy(a)
print(a, c)
a[1].append(5)
print(a, c)
