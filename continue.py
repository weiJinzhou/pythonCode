#!/usr/bin/env python3
while True:
    n = int(input("Please enter an Integer: "))
    if n < 0:
        continue  #  这会返回到循环开始处执行
    elif n == 0:
        break  #  这会退出循环，终止游戏
    print("Square is ", n ** 2)
print("Goodbye")
