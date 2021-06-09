# coding: utf-8

cartoon = []
history = []
code = []

new_cartoon = ('a', 'b', 'c')
new_history = ('Chinese history', 'Japanese history', 'Western history')
new_code = ('python', 'django', 'flask')

cartoon.extend(new_cartoon)
history.extend(new_history)
code.extend(new_code)

print(cartoon, history, code)

history.extend(cartoon)
del cartoon
print(history)

test = []
test.extend({'name': 'meiqi', 'age': 20})
print(test)
