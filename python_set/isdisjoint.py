# coding: utf-8

company_not_allow = {'女', '喝酒', '抽烟', '睡懒觉'}

player1 = {'男', '跑步', '朝气', '喝酒'}
player2 = {'女', '生活规律', '跆拳道'}
player3 = {'男', '太极拳'}
player4 = {'男', '空手道', '年轻'}

print(company_not_allow.isdisjoint(player1))
print(company_not_allow.isdisjoint(player2))
print(company_not_allow.isdisjoint(player3))
print(company_not_allow.isdisjoint(player4))
