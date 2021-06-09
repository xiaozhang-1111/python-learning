# coding: utf-8

students = {
    'meiqi': '到',
    'xiaomu': '在哦',
    'xiaoyun': '在',
    'xiaogao': '在呢'
}

print('xiaogao在吗')
xiaogao = students.popitem()
print('{}喊：{}'.format(xiaogao[0], xiaogao[1]))
print('xiaoyun在吗')
xiaoyun = students.popitem()
print('{}喊：{}'.format(xiaoyun[0], xiaoyun[1]))
print('xiaomu在吗')
xiaomu = students.popitem()
print('{}喊：{}'.format(xiaomu[0], xiaomu[1]))
print('meiqi在吗')
meiqi = students.popitem()
print('{}喊：{}'.format(meiqi[0], meiqi[1]))
print(students)
