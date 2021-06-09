# coding:utf-8

user_info = {'name': '小木同学', 'age': 10, 'top': '180cm'}

result = 'name' in user_info
print(result)

result = 'hope' in user_info
print(result)

result = 'hope' not in user_info
print(result)

count = len(user_info)
print(count)

result_bool = bool(user_info)
print(result_bool)

empty_dict = {}
print(bool(empty_dict))

print(type(dict(empty_dict)))
print(max(user_info))
print(min(user_info))
