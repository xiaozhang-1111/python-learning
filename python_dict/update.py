# coding: utf-8

user = {'username': 'meiqi', 'age': 20, 'top': 170}
xiaomu = {'username': 'xiaomu', 'age': 10, 'top': 160, 'sex': 'male'}
user.update(xiaomu)
print(user)

value = user.setdefault('username', 'xiaoyun')
value = user.setdefault('birthday', '2020-1-1')
print(user, value)

# print(user)
# user['username'] = 'xiaomu'
# print(user)
# user['top'] = 160
# user['age'] = 10


