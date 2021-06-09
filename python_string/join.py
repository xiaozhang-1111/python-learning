# coding: utf-8

li = ['apple', 'peach', 'banana', 'pear']
print(','.join(li))
print('.'.join(li))

x = 'aaa     bb   c d e  fff       '
print(x.split())
print(' '.join(x.split()))  # 删除字符串中多余的空白字符，连续多个空白字符只保留一个


def equavilent(s1, s2):  # 判断两个字符串在Python意义上是否等价
    if s1 == s2:
        return True
    elif ' '.join(s1.split()) == ' '.join(s2.split()):
        return True
    elif ''.join(s1.split()) == ''.join(s2.split()):
        return True
    else:
        return False


print(equavilent('pip list', '  pip    list  '))
