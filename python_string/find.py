# coding:utf-8

info = 'python is a good code'

result = info.find('a')
print(result)
result = info.find('ok')
print(result)

result = info.index('a')
print(result)
# result = info.index('ok')
# print(result)

s = 'apple peach banana peach pear'
print(s.find('peach'))
print(s.find('peach', 7))
print(s.find('peach', 7, 20))
print(s.rfind('p'))
