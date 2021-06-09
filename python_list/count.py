# coding: utf-8

animals = ['小猫', '小狗', '龙猫', '小猫', '鹦鹉', '小狗', '兔子', '小猫']

cat = animals.count('小猫')
dog = animals.count('小狗')
longmao = animals.count('龙猫')
rabbit = animals.count('兔子')

print('我家院子的动物有%s只小猫，有%s只小狗，有%s只龙猫，有%s只兔子' % (cat, dog, longmao, rabbit))
print('但是没有松鼠，所以有松鼠%s只' % animals.count('松鼠'))

animals_dict = [
    {'name': 'dog'},
    {'name': 'dog'},
    {'name': 'cat'}
]

dog_dict_count = animals_dict.count({'name': 'dog'})
print('小狗在动物的字典中有%s只' % dog_dict_count)

animals_tuple = ('小猫', '小狗', '龙猫', '小猫', '鹦鹉', '小狗', '兔子', '小猫')
cat = animals_tuple.count('小猫')
dog = animals_tuple.count('小狗')
longmao = animals_tuple.count('龙猫')
rabbit = animals_tuple.count('兔子')

print('我家院子的动物有%s只小猫\n\t\t有%s只小狗\n\t\t有%s只龙猫\n\t\t有%s只兔子' % (cat, dog, longmao, rabbit))
