import random as r
n = r.randint(1, 10)
print(n)

m = eval(n)
print(type(m))


for i in range(3):
    player = eval(input("input"))
    print(type(player))
    if n == player:
        print("yes")
        break
    elif player > n:
        print("bigger")
    elif player < n:
        print("smaller")
    else:
        print("fuck")
