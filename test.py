# coding: utf-8

string = input('请输入一行字符串：')
alpha_num, digit_num, space_num, other_num = 0, 0, 0, 0
for i in string:
    if i.isalpha():
        alpha_num += 1
    elif i.isdigit():
        digit_num += 1
    elif i.isspace():
        space_num += 1
    else:
        other_num += 1
print("字符串中字母个数为：%s，数字个数为：%s，空格个数为：%s，其他字符个数为：%s" % (alpha_num, digit_num, space_num, other_num))
