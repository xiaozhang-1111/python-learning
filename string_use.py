# coding:utf-8

info = 'python是一种语言'

print(info * 2)
print(info[8])
print(info[4:8])

result = '语言' in info
print(result)

result = '美丽' in info
print(result)

info2 = 'Python is a good code'

print(max(info2))
print('.', min(info2), '.')

info3 = '天气好 要多锻炼身体，'
info4 = '多锻炼身体 会更健康'

new_str = info3 + info4 + '！'
print(new_str)
print(len(new_str))
length = len(new_str)
print(type(length))
