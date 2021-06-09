# coding: utf-8

books = []
print(id(books))
books.append('python入门')
print(books)
print(id(books))

number = 1.1
tuple_test = (1,)
dict_test = {'name': 'meiqi'}

books.append(number)
books.append(tuple_test)
books.append(dict_test)
books.append('django')
books.append('')
books.append(True)
print(books)
