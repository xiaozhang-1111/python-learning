# codidng: utf-8

projects = {
    'ipad': {'name': 'ipad', 'price': 3000, 'desc': '平板电脑'},
    'iphone': {'name': 'iphone', 'price': 5000, 'desc': '智能手机'},
    'pc': {'name': 'pc', 'price': 8000, 'desc': '台式电脑'},
    'mac': {'name': 'mac', 'price': 9000, 'desc': '苹果电脑'}
}

print(projects.keys())

print('一个中学生购买了%s，价格是%s' % (projects['pc']['name'], projects['pc']['price']))
projects.pop('pc')
print(projects.keys())

result = projects.pop('mac')
print('一个程序员购买了{}，价格是{}'.format(result['name'], result.get('price')))
print(projects.keys())

print('{}和{}都被卖出去了，一共{}元'.format(
    projects['ipad']['name'], projects['iphone']['name'],
    projects['ipad']['price'] + projects['iphone']['price']
))
projects.clear()
print(projects.keys())

del projects
# print(projects)
