'''

set 集合
不支持重复元素
内容无序 : 不支持下标索引访问
但是允许修改
'''
import setuptools.dist

set1 = {1, 2, 3, 4, 5, 6, 6, 1, 1, 1}
print(set1)

# .add()添加元素
set1.add("1")
print(set1)

# .remove(element) 移除元素
set1.remove(1)
print(set1)

# 随机取出元素 .pop()  从集合中随机取出一个元素
# 会得到一个元素的结果， 同时集合本身被修改， 元素被移除
element = set1.pop()

# .clear() 清空集合

# set1.difference(set2) 取出set1和set2中的差集（set1中有，set2中没有的）
# 得到一个新集合，set1, set2不变
set1 = {1, 2, 3}
set2 = {2, 3, 4}
set3 = set1.difference((set2))
print(set3)

# 消除两个集合的交集, 将set1更新为差集 在set1内，删除和set2相同的元素
# set1被改变，set2不变

set1 = {1, 2, 3}
set2 = {1, 5, 6}
set1.difference_update(set2)
print(set1)

# 合并两个集合
# 将集合1和集合2组合成新的集合 结果为一个新的集合,不会修改原有集合
set1 = {1, 2, 3}
set2 = {1, 2, 5}
set3 = set1.union(set2)
print(set3)

# 统计集合的数量 len()函数
set1 = {1, 2, 3, 4, 5, 6, 7}
num = len(set1)
print(num)

# 集合的遍历
# 集合不支持下标索引 所以不支持while循环 但是支持for循环

for element in set1:
    print(element)

# practice
pre_list = {'heima', 'chuanzhi', 'itma', 'itcast', 'best', 'itma'}
my_list = set()
for ele in pre_list:
    my_list.add(ele)

for element in my_list:
    print(element)

