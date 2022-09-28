a = 10

while(a > 5):
    print(a)
    a -= 1

str1 = "abcdefghijklmn"

for char in str1:
    print(char)

list1 = ['a', 'b', 'c', 'd']

for i in list1:
    print(i)


# range(开头 = 0， 结尾， 步长 = 1）
print(list(range(0, 10, 2)))

for i in range(0, len(list1), 1):
    print(i)

for i in range(len(list1)):
    print(i)


# break 