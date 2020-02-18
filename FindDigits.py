#!/usr/bin/env python3
# method 1
print('Method 1:')
# 打开的文件
fobj = open('/tmp/String.txt')
robj = fobj.read()
res = ""
for char in robj:
    if char.isdigit():
        res += char
print(res)
# 关闭打开的文件
fobj.close()

# method 2
print('Method 2:')
res = ""
# 打开并读取文件里的字符串
with open('/tmp/String.txt') as f:
    s = f.readline()
    while s:
        for c in s:
            if c.isdigit():
                res += c
        s = f.readline()
print(res)
