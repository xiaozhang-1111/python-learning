# coding: utf-8

user_info = {
    'id': 1,
    'username': 'meiqi',
    'password': 'abcdefg',
    'created_time': '2021-1-1 13:13:13',
    'birthday': None
}

values = []
values.append(user_info['id'])
values.append(user_info['username'])
values.append(user_info['password'])
# values.append(user_info['created_time'])
values.append(user_info.get('created_time', '2000-11-11'))
# values.append(user_info['birthday'])
values.append(user_info.get('birthday', '2000-11-11'))
print(values)



# values.append(user_info.get('birthday', '1986-01-01'))
# print(values)
