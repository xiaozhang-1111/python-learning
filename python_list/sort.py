# coding: utf-8

shu = '01鼠'
niu = '02牛'
hu = '03虎'
tu = '04兔'
long = '05龙'
she = '06蛇'
ma = '07马'
yang = '08羊'
hou = '09猴'
ji = '10鸡'
gou = '11狗'
zhu = '12猪'

shengxiao = []
shengxiao.append(long)
shengxiao.append(shu)

shengxiao.append(zhu)
shengxiao.append(hu)
shengxiao.append(niu)
shengxiao.append(ma)
shengxiao.append(tu)
shengxiao.append(yang)
shengxiao.append(she)
shengxiao.append(gou)
shengxiao.append(ji)
shengxiao.append(hou)

print(shengxiao)
print(len(shengxiao))
shengxiao.sort()
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)
shengxiao.sort(reverse=True)
print(shengxiao)

mix = ['python', 1.2, {'name': 'xiaozhang'}]
# mix.sort()
# print(mix)
