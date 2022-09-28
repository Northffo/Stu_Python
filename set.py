# 自动排序和去重
set1 = {1, 2, 3, 5, 2}

print(set1)

set1 = set((2, 3, 1, 2, 3, 4, 5, 7))
print(set1)

set1 = {1, 2, 3, 4}
set1.add(5)
set1.discard(3)    # 删除元素
print(set)

set1 = {1, 2, 3, 4, 5, 6}
set2 = {1, 2, 4}

print(set1.intersection(set2))       # 输出两个集合共有的元素
print(set1.difference(set2))        # 输出非共有的元素, 1有2没有的
print(set2.issubset(set1))          # 判断这个集合是否是目标集合的子集
