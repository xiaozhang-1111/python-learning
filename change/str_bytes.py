# coding: utf-8

a = 'hello xiaomu'
print(a, type(a))

b = b'hello xiaomu'
print(b, type(b))

print(b.capitalize())
print(b.replace(b'xiaomu', b'dewei'))
print(b[:3])
print(b.find(b'x'))

print(dir(b))

c = 'hello 小木'
d = c.encode('utf-8')
print(d, type(d))
print(d.decode('utf-8'))


print('慕卿'.encode('utf-8').decode('utf-8'))
s = '中国内蒙古自治区adfda'
print(len(s))

