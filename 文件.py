# 操作文件
# 打开文件或者创建一个新文件 open（name， mode， encoding）
# name：要打开的目标文件名的字符串（可以包含文件所在的具体路径） 如果只给文件名,默认是跟本文件同一层级
# mode：要打开文件的模式（访问模式）：只读“r” 写入"w" 追加“a”等等
# r:以只读方式打开文件， 文件的指针会放在文件的开头，这是默认模式
# w:打开一个文件用于写入，如果该文件已存在则打开文件，并从头开始编辑，原有内容会被删除，不存在则新建文件
# a:打开一个文件用于追加.如果文件已存在,新的内容将会被写到已有内容之后,不存在则新建文件
# encoding：编码格式（推荐UTF-8）

# 打开文件
f = open("D:/test.txt", "r", encoding="UTF-8")
print(type(f))

# 读取文件  --readLines()
# .read(num)    # num表示要从文件中读取数据的长度（单位是字节）， 如果没有传入num，表示读取所有
# .readlines()  # readlines() 可以按照行的方式把整个文件中的内容进行一次性读取，并且返回的是一个列表，其中每一行元素的数据为一个元素
# 文件内容打开之后，无论调用什么方法，都会续接上一次读取文件的方法的位置
# print(f.read())
# print(f.read(10))

lines = f.readlines()   # 读取全部行封装到列表里面
print(lines)

# .readline()   一次读取一行内容

f = open("D:/test.txt", 'r', encoding="UTF-8")
# line1 = f.readline()
# print(line1)

# for循环读取文件行
for line in f:
    print(f"line = {line}")

# 文件的关闭
# .close()  如果不调用close,这个文件就会在一直被Python程序占用
import time
#time.sleep(50000)

f.close()

