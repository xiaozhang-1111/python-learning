# coding: utf-8

project = {'id': 1, 'name': 'ipad', 'price': 3000, 'count': 50}

keys = list(project.keys())
values = list(project.values())
print(keys)
print(values)

print('{} | {} | {} | {}'.format(keys[0], keys[1], keys[2], keys[3]))
print('{}  | {} | {}  | {}'.format(values[0], values[1], values[2], values[3]))
