# coding:utf-8

s = 'apple,peach,banana,pear'
print(s.split(','))
print(s.partition(','))
print(s.rpartition(','))
print(s.rpartition('banana'))

s = '2021-06-06'
t = s.split('-')
print(t)
print(list(map(int, t)))

s = '\n\nhello\t\t world \n\n\n My name is Zhang.'
print(s.split(None, 1))
print(s.rsplit(None, 2))
print(s.split(maxsplit=6))
print(s.split())
print(s.split(' '))
