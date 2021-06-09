# coding: utf-8

names = ('meiqi', 'xiaozhou', 'xiaozhang')

names_add = names + names
names_c = names * 10

print(names_add)
print(names_c)
print(len(names_c))

names += ('abc', )
print(names)
names *= 10
print(names)

names_list = ['meiqi', 'xiaozhang']
names_list += ['xiaowang']
print(names_list)
names_list *= 5
print(names_list)

print('meiqi' in names_list)
print('meiqi' not in names_list)
