# coding:utf-8

info = '         my name is meiqi         '
new_info = info.strip()
print('.' + new_info + '.')

info01 = 'my name is meiqi'
new_info01 = info01.strip(info01)
print(new_info01)
print(len(new_info01))

new_str = 'abcde'
print(new_str.strip('a'))
print(new_str.strip('e'))
