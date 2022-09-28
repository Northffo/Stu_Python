list1 = [1, 2, 3, 4, 5]   # 每一项可以放不同的数据类型

print(list1[0])

# append 尾插
list1.append(6)
print(list1)

# len 获取列表长度
print(len(list1))

# pop 括号里的参数是元素下标
list1.pop(0)
print(list1)

# insert(位置， 元素）
list1.insert(1, 0)
print(list1)

# sort 排序 默认升序
list1.sort()
print(list1)

# index 返回某个元素的下标
print(list1.index(2))

# reverse 反向排列
list1.reverse()
print(list1)

# remove 删掉某一个元素，参数是要删掉的元素
list1.remove(0)
list1.reverse()
print(list1)

# -----------------------------元组----------------------------
tuple1 = (1, 2, 3)
print(tuple[0])

# 列表和元组可以相互转换
print(tuple1)
print(list(tuple1))



