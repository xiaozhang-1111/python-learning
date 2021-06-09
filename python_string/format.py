# coding: utf-8

info = 'my name is %s, my age is %s'

name01 = '小木'
age01 = 10
name02 = 'meiqi'
age02 = 33
print(info % (name01, age01))
print(info % (name02, age02))

message = '您好，今天是%s，您的手机号码%s已经欠费了，请尽快充值。'
print(message % ('星期一', 13755552222))

print(message % (123456, '星期二'))
print(message)

books = ['python', 'djange', 'flask']
info02 = 'my name is %s, my age is %s, my books are %s'
print(info02 % (name01, age01, books))

dict01 = {'a': 'a', 'b': 'b'}
print('dict is %s' % dict01)

info03 = 'my name is {0}, my age is {1}, my books are {2}'
print(info03.format(name02, age02, books))

info04 = f'my name is {name01}, my age is {age02}'
print(info04)

print(info03.format('dewei', 22, ['python']))

print('{:%}'.format(0.35))
print('{:.3}'.format(1/3))
print('{:,}'.format(10000000))

position = (2, 3, 1)
print('x={0[0]}, y={0[1]}, z={0[2]}'.format(position))

weather = [('Monday', 'rainy'), ('Tuesday', 'sunny'), ('Wednesday', 'sunny'), ('Thursday', 'rainy'), ('Friday', 'cloudy')]
formatter = 'Weather of {0[0]} is {0[1]}.'.format
# for item in map(formatter, weather):
#     print(item)
for item in weather:
    print(formatter(item))
