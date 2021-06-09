# coding:utf-8

info = '''
        The Python Software Foundation (PSF) is a 501(c)(3) non-profit corporation 
        that holds the intellectual property rights behind the Python programming language. 
        We manage the open source licensing for Python version 2.1 and later and own and 
        protect the trademarks associated with Python. We also run the North American PyCon 
        conference annually, support other Python conferences around the world, and fund 
        Python related development with our grants program and by funding special projects.
'''

a = info.count('a')
b = info.count('b')
c = info.count('c')
d = info.count('d')
e = info.count('e')
f = info.count('f')

print(a, b, c, d, e, f)
number_list = [a, b, c, d, e, f]
print(number_list)
print('在列表中，最大的数是', max(number_list))

number_dict = {
    'a': a,
    'b': b,
    'c': c,
    'd': d,
    'e': e,
    'f': f
}
print('每个成员对应的数值分别是', number_dict)
