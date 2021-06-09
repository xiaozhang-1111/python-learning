# coding: utf-8

from pypinyin import lazy_pinyin, pinyin

print(lazy_pinyin('张美琪'))
print(lazy_pinyin('张美琪', 1))
print(lazy_pinyin('张美琪', 2))
print(lazy_pinyin('张美琪', 3))

print(lazy_pinyin('重要', 1))
print(lazy_pinyin('重阳', 1))
print(pinyin('重阳'))
print(pinyin('重阳节', heteronym=True))
