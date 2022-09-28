# dictionary  ..  键值对

dict1 = {"name": "Jone", "height": 170}

print(dict1["height"])

# len 获取键值对的个数
# keys 获取所有的键
# values 获取所有的值
# pop 删除，括号里是键
# 如果要添加可以直接中括号然后加
print(dict1.keys())
dict1["gender"] = "nan"

dict1.pop("name")
print(dict1)



