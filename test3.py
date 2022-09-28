def cal(num1, num2):
    '''
    函数的注释写在函数体之前，
    :param num1: 对形参说明
    :param num2: 对形参说明
    :return: 对返回值说明
    '''
    return num1 + num2

print(cal(1, 2))

# 如果函数没有使用return语句返回数据，那么函数会返回None
# None的应用价值: 用在函数没有返回值上
#               用在if判断上，None相当于False

# 局部变量：定义在函数体内部的变量 只在函数体内部生效
def test():
    global num     # 将num定义为全局变量
    num = 200
    print(f"num = {num}")

test()


# ATM案例
money = 5000000
name = "user"

def check():
    print(f"your id user have {money}")
    main()

def save():
    tmp = eval(input("save how much"))
    global money    # 如果不加这个声明 money只会是一个局部变量
    money += tmp
    check()
    main()

def qu():
    tmp = eval(input("qu how much"))
    global money
    money -= tmp
    check()
    main()

def main():
    global name
    if(name == "user"):
        name = input("your name:")
    print("check then press 1")
    print("save then press 2")
    print("qu then press 3")
    print("exit then press 0")
    op = eval(input("your operation"))
    print("hello, %s" % name)
    if(op == 1):
        check()
    elif op == 2:
        save()
    elif op == 3:
        qu()
    elif op == 0:
        exit()

main()