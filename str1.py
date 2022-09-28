string1 = "hello world"

print(string1[2])

# len = length 获得字符串长度
print(len(string1))

# capitalize 把我们字符串的第一个字母大写
print(string1.capitalize())

# upper 把我们字符串所有字母大写
print(string1.upper())

# lower 把我们字符串所有字母小写
print(string1.lower())

# replace 把第一个匹配的字符串换到第二个
print(string1.replace("world", "python"))

# find return第一个字母匹配的位置，否则return -1
print(string1.find("hello"))

# boolean
a = True
b = False

# isupper 判断字符串中字母是否全部大写
print(string1.isupper())

# split 分割字符串 ，把字符串切割成列表的形式
str1 = "hello, world"
print(str1.split('o'))
print(str1.split('o', 1))  # 后面的参数是最大的切割次数




