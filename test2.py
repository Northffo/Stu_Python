#name = input("who are you\n")
#print("i see, you are %s" % name)

# input()语句把所有的输入都看成字符串
# 从键盘输入两个整数
'''
x = int(input("input double nums"))

y = int(input("another"))

print(x + y)'''

# eval 将任意含有数字的字符串转化为有效的数字 待转化的字符串应只含有数字

# range语句
# range(num) 一个从0开始，到num结束的数字序列 [0, num)
# range(start, stop, step)  // 创建一个整数列表， start && step 可省略 范围为[start, stop）

# 有几个偶数
cnt = 0
num = 100
for i in range(1, num):
    if(not (i & 1)):
        cnt += 1

print(cnt)

# 九九乘法表
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={i*j}", end=" ")           # print(*object, sep = ' ', end = '\n', file = sys.stdout, flush = False)
        if(i == j):
            print("")
