# coding: utf-8

drivers = ['meiqi', 'xiaomu', 'xiaoming', 'xiaoman']
testers = ['xiaomu', 'xiaoman', 'xiaogang', 'xiaotao']

drivers_set = set(drivers)
test_set = set(testers)

drivers_diff = drivers_set.difference(test_set)
print(drivers_diff)
