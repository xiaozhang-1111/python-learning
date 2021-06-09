# coding:utf-8

title = '小木学校的春游'

class_count = 51
boys = 28
girls = 23

every_body_pay = 35.5

start_time = 8.00
bus_count = 2
site_every_bus = 30

come_park_time = 10.33

lunch_time = 12.0
lunch_pay = 25.5

leave_park_time = 3.05

bus_pay = 5

come_back_school_time = 5.00

back_pay = 5

if __name__ == '__main__':
    print(title)
    print('小木的班级有', class_count, '人')
    print('男生有', boys, '人')
    print('女生有', girls, '人')
    print('每人支付', every_body_pay, '元')
    print('出发的时间是早上', start_time)
    print('出行需要', bus_count, '辆公交大巴')
    print('我们到达公园的时间是', come_park_time)
    print('吃午饭的时间是', lunch_time)
    print('每人支付伙食费', lunch_pay, '元')
    print('离开公园的时间是', leave_park_time)

    print('大巴支付的费用是每人', bus_pay, '元')

    print('下午', come_back_school_time, '点到达学校')
    print('这一天小木同学花费了', 30.5, '元')
    print('最后退回', back_pay, '元')

    print(type(come_back_school_time))
    print(type(every_body_pay))
    print(type(site_every_bus))
