# coding: utf-8

students = [
    {'name': 'meiqi', 'age': 20, 'top': 170},
    {'name': 'xiaozhang', 'age': 21, 'top': 160},
    {'name': 'xiaogao', 'age': 18, 'top': 188},
    {'name': 'xiaoyun', 'age': 19, 'top': 165}
]

print('当前的同学顺序是{}'.format(students))
students.reverse()
print('座位更换之后的顺序是{}'.format(students))
