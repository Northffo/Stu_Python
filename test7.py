x = {1: 'a', 2: 'b', 3: 'c'}
y = {1, 3, 4}
print(x.keys() - y)
print(x.items())
# keys() & keys() 查找键的交集
# a.keys() - b.keys() 查找a中存在 b不存在的键
# a.items() & b.items() 查找键值对的交集


print(list(map(str, [1, 2, 3])))
# map(function, iterable, ...) 将function依次作用在list的每一个元素上,得到一个新list并返回
# zip([iterable, ...])  将对象中对应的元素打包成一个个元组,然后返回有这些元组组成的列表


# list 复制[地址,深浅拷贝]
# 赋值 将a的之地也一并复制过去, 当a发生变化时,b也会发生变化
a = [1, 2, [3, 4], 5]
b = a
print(a, b)
a[0] = 0
print(a, b)


# 浅拷贝方法
a = [1, 2, [3, 4], 5]
c = a[:]
d = a.copy()
e = list(a)
import copy
f = copy.copy(a)
# 修改a
a[0] = 0        # c, d, e, f不变
# 修改a的子列表
a[2][1] = 8     # c, d, e, f改变
'''
浅复制要分两种情况进行讨论：
1）当浅复制的值是不可变对象（字符串、元组、数值类型）时和“赋值”的情况一样，对象的id值（id()函数用于获取对象的内存地址）与浅复制原来的值相同。

2）当浅复制的值是可变对象（列表、字典、集合）时会产生一个“不是那么独立的对象”存在。有两种情况：

     第一种情况：复制的对象中无复杂子对象，原来值的改变并不会影响浅复制的值，同时浅复制的值改变也并不会影响原来的值。原来值的id值与浅复制原来的值不同。

     第二种情况：复制的对象中有复杂子对象（例如列表中的一个子元素是一个列表），如果不改变其中复杂子对象，浅复制的值改变并不会影响原来的值。 但是改变原来的值中的复杂子对象的值会影响浅复制的值。
'''


x = [[1]] * 3
x[0][0] = 5
print(x)

x = [1, 3, 2]
y = x.sort()
print(x, y)
# sort()没有返回值, 改变对象本身, sorted()才有返回值, 不改变对象本身, 返回一个新的列表


print(list(zip([1, 2], [3, 4])))

print(sorted([111, 2, 33], key = lambda x: len(str(x))))

print(list(map(list, zip([1, 2, 3], [4, 5, 6]))))

print({1: 'a', 2: 'b', 3: 'c'}.get(4, 'd'))

x = list(range(10))
print(x[-4:])

x = {1: 2, 2: 3}
print(x.get(3, 4))

print([1, 2, 3][-5:])     # 切片操作时,起始偏移量跟终止偏移量不在[0:长度]这个范围时,会被当成0,和长度

a = sum([x**2 for x in range(1, 5)])
print(a)

print({index for index, value in enumerate([3, 5, 3, 7]) if value == 3})

x = [1, 2]
print(list(enumerate(x)))

print(list(range(6))[::-2])

x = [3, 5, 7]
x[len(x):] = [1, 2]
print(x)        # [3, 5, 7, 1, 2]

my_list = [1, 2, 3, 4, 5, 6]
print(my_list[1:3])

x = [3, 5, 7]
x[0:0] = [8]
print(x)

x = 3==3, 5   # 不同元素之间用 , 隔开说明这是一个元组
print(x)

x = 3,        # 同上
print(x)

print([x for x in[1, 2, 3, 4, 5]if x<3])

x = range(1, 4) #
y = range(4, 7)
print(sum([i*j for i, j in zip(x, y)]))

print(3 in [1, 2, 3, 4])    # True--in： item in list  检查item是否是在指定的序列中
print([3] in [1, 2, 3, 4])  # False


# print(len(map(str, range(5))))  # map对象不支持内置函数len()

x = map(str, range(5))      # ['0', '1', '2', '3', '4'] # map（）返回的是一个迭代器
print(x)
print(list(x))
print(x)
x = list(x)
print(x)

x = [1, 2, 3, 4, 5]
del x[:3]
print(x)

print(sorted([1, 2, 3], reverse = True) == reversed([1, 2, 3]))
