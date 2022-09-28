# dict

# dict1 = {}  定义空字典， 所以定义空集合的时候不能直接用{}定义
dict2 = dict()
dict1 = {'wlh':99, 'wyf':98, 'zjl':88}

print(dict1)

# 字典中不允许重复 重复添加的元素会把前面的覆盖掉
dict1 = {'wlh': 99, 'wlh': 77, 'ljj': 88}
print(dict1)

# 通过key获取value
dict1 = {'wlh':99, 'wyf':98, 'zjl':88}
score = dict1['wlh']          # 注意是中括号
print(score)

# 字典的key和value是可以为任意类型 （key不可为字典） 所以字典是可以嵌套的
stu_score_dict = {
    "wlh": {'chinese': 77,
            'math': 66,
            'english': 33
            },
    "zjl": {
        "chinese": 99,
        "math": 88,
        "english": 55
    }
}

print(stu_score_dict)

# 从嵌套的字典中获取数据
score = stu_score_dict["zjl"]["chinese"]
print(score)

# 字典的操作
# 新增元素 || 更新元素
stu_score_dict["zs"] = {
    "chinese": 98,
    "math": 44,
    "english": 44
}                     # 如果原先字典中没有这个key，那么会新增一个元素

# 删除元素 dict.pop(key) 获取指定key的value 同时字典被修改 指定key的数据被删除
# 清空字典 dict.clear()
stu_score_dict = {
    "wlh": {'chinese': 77,
            'math': 66,
            'english': 33
            },
    "zjl": {
        "chinese": 99,
        "math": 88,
        "english": 55
    }
}
score = stu_score_dict.pop('zjl')
print(score)
print(stu_score_dict)
stu_score_dict.clear()

# 获取全部key dict.keys()
my_dict = {"zjl": 99, "wlh": 23, "ljj": 31}
keys = my_dict.keys()
print(keys)

# 遍历字典
for key in keys:
    print(f"{key}: {my_dict[key]}")

for key in my_dict:
    print(f"2: {key}: {my_dict[key]}")

# 统计字典的元素数量 len()

# eg：
engeer = {
    "wlh": {
        "部门": "科技部",
        "工资": 3000,
        "level": 1
    },
    "zjl": {
        "部门": "市场部",
        "工资": 5000,
        "level": 2
    },
    "ljj": {
        "部门": "市场部",
        "工资": 7000,
        "level": 3
    },
    "zxy": {
        "部门": "科技部",
        "工资": 4000,
        "level": 1
    },
    "ldh": {
        "部门": "市场部",
        "工资": 6000,
        "level": 2
    }
}

keys = engeer.keys()
print(engeer)
for key in engeer:
    if engeer[key]["level"] == 1:
        engeer[key]["工资"] += 1000
        engeer[key]["level"] += 1


print(engeer)


