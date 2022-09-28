print(sum([i*i for i in range(3)]))       # 5 range(start, stop, step)  // 创建一个整数列表， start && step 可省略 范围为[start, stop）

x = [1, 2]
y = [3, 4]
print(x + y)                              # [1, 2, 3, 4]

print(max([1, 2, 3], [2, 1, 3, 0], [3, 2, 1]))    # max里面都是元组或者列表时，取第一个最大值 并返回相应列表

import random
print(len(random.choices(range(100), k = 20)))     # random.choices(list,weights=None,*,cum_weights=None,k=1) 从list中随机选取k次数，weight为相对权重（选取概率），cum_weight为累加权重
                                                   # random.choice为从list中随机抽取一个元素

5                                                  # 一个数字5也是合法python表达式

print(5.1 % 2)                                     # % 也可以对浮点数取余

x = ['aaaa', 'bc', 'd', 'b', 'ba']
print(sorted(x, key = len))                        # sorted(iterable, /, *, key=None, reverse=False)  // key是排序的依据， reverse 代表升序还是降序 默认升序

print([1, 2, 1, 2, 1][1 :: 2])                     # [m::n] 从a[m]开始，每跳n个取一个

print("1111", 2)
print(int(4 ** 0.5))
print(-17 // 4)                                    # // 表示向下取整的除法
print('123' * 3)
print(chr(ord('D') + 2))                           # F ord为把字符从ascii码转化为数字，
print(list(filter(None, [-3, 0, 3])))              # filter(function,iterable) 过滤掉不符合条件的函数， function为判断函数， 当容器中元素返回为true时放到新列表中
# print(3 == 3 is not True)                          # is 与 is not 判断是否引用的同一个对象， id(a) == id(b)
## set(b) < set(a) # a是否包含b，<= 则表示是否是子集
print(sum(map(int, str(123456))))                  # map(function, iterable,......) 将func函数一次作用于iterable中每个元素
print(bool([]))                                    # bool在传入列表元组字典时判断是否为空
print(max(['121', '34']))
print(bool(map(str, range(8, 5))))
print(int("123"))
print(sum(map(lambda num:num>3, [1, 2, 3, 4, 5])))
print(1, 2, 3, sep = '.')
print(eval('3 * 2' + '22'))                        # eval()函数先进行字符串拼接在进行加减乘除操作
print(3 in range(1, 10, 2))
print(isinstance("3.14", (int , float, complex)))
print(int("101", 2))

'''
print(con1 ,con2, con3,....)
用tpye语句可以可以查看变量的类型
字符串如果只有数字就可以转换成数字
// 整除符号

'''

# 字符串拓展 单引号定义法 双引号定义法 三引号定义法
name = 'a'
name = "aaa"
name = """a"""

# 可以用转义符\ 来解除引号的效用
#字符串的拼接
print("abc" + "def")
name = "hm"
print("myname = " + name)
print("myname =", name)   # 如果用，  则前面一个会自动加一个空格

# 字符串跟数字是无法直接拼接的 wrong: print("name" + 123)

# 字符串格式化
name = "hm"
message = "xue it jiulai %s" % name   # 用数据类型占位来拼接， #s 将内容转换成字符串 %d, %f
print(message)

class_num = 57
avg_salary = 12121
message = "time = %s, salary = %s" % (class_num, avg_salary)
print(message)

# 格式化的精度控制 用m.n控制数据的宽度和精度 m控制宽度， 若m比数字本身宽度小则m不会生效，若宽度不够会在前面补空格 n控制精度
# %5.2f
num1 = 11
num2 = 11.34
print("%5d, %.1f" % (num1, num2))

# 字符串格式化 快速格式字符串 不理会类型，做不了精度控制
name = "bk"
set_up_year = 2006
stock_price = 19.99
print(f"name is {name}, set up in {set_up_year}, and price = {stock_price}")

# 表达式格式化
print("type(string) = %s" % type("aaa"))

# 股价计算
name = "user"
stock_price = 17.65
stock_code = "E3FF3"
stock_price_daily = 1.21
growth_days = 5

print(f"name :{name}\tstock_price : {stock_price}\nstock_price_daily : {stock_price_daily}")
print(f"stcok")


