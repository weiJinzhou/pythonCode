#!/usr/bin/env python3
n = int(input('Enter the number of students: '))
data = {}  # 用来存储数据的字典变量
subjects = ('Physics', 'Maths', 'History')  # 所有科目
for i in range(n):
    name = input('Enter the name of the student {}: '.format(i + 1))  # 获得学生姓名
    marks = []
    for x in subjects:
        marks.append(int(input('Enter marks of {}: '.format(x))))  # 获得每一科成绩
    data[name] = marks
for x, y in data.items():  # 输出学生成绩并判断是否通过考试
    total = sum(y)
    print("{}'s total marks {}".format(x, total))
    if total < 120:
        print(x, "failed :(")
    else:
        print(x, "passed :)")
