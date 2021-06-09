# coding: utf-8

shops = ['可乐', '洗发水', '可乐', '牛奶', '牛奶', '牙膏', '牙膏']

print('超市中有%s件可乐，%s件洗发水，%s件牛奶，%s件牙膏' %
      (shops.count('可乐'), shops.count('洗发水'), shops.count('牛奶'), shops.count('牙膏')))
print('购买一件洗发水')
shops.remove('洗发水')
print('现在洗发水还剩%s件' % shops.count('洗发水'))
shops.remove('可乐')
print('现在可乐还剩%s件' % shops.count('可乐'))

del shops

print(shops)
