# *args 传参    形成元组
# **kwargs 传参 形成字典

# 匿名函数
# 函数作为参数传递

def test_func(cmpt):
    ret = cmpt(1, 2)
    print(ret)

def cmpt(x, y):
    return x + y

test_func(cmpt)

# lambda函数
# def关键字定义函数: 定义带有名称的函数
# lambda关键字： 定义匿名函数
# 有名称的函数， 可以基于名称重复使用
# 无名称的函数，只可临时使用一次


# lambda 传入参数： 函数体（一行代码）
# 不用写return语句 ，默认return
test_func(lambda x, y: x + y)       # 作用范围只在这一次调用中有效



