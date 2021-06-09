# coding: utf-8

a = ['meiqi', 'xiaomu', 'xiaohua', 'xiaoguo']
b = ['xiaohua', 'meiqi', 'xiaoman', 'xiaolin']
c = ['xiaoguang', 'xiaobai', 'meiqi', 'xiaoyuan']

a_set = set(a)
b_set = set(b)
c_set = set(c)

result = a_set.intersection(b_set, c_set)
xiaotou = list(result)
print('{}是这个小偷'.format(xiaotou[0]))
