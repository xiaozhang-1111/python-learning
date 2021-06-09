# coding: utf-8

default = {'a': None, 'b': 1, 'c': 0, 'd': ''}

print('a' in default)
print(default['a'])
print(bool(default.get('a')))
print(bool(default.get('b')))
