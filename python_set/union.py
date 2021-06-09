# coding: utf-8

a_school = ['周五半天', '免费周末培训', '周五休息']
b_school = ['早放学', '少留作业', '座椅舒服']
c_school = ['少留作业', '周五半天', '伙食改善']

a_set = set(a_school)
b_set = set(b_school)
c_set = set(c_school)

# help_data = a_set.union(b_set, c_set)
help_data = a_set.union(b_school, c_school)
print(help_data)
print(len(help_data))
