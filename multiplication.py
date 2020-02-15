#!/usr/bin/env python3
i = 1
print('-' * 50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:5d}".format(i * n), end='')
        n += 1
    print()
    i += 1
print('-' * 50)

for x in range(1, 10):
    for y in range(1, x + 1):
        print("{}*{} = {:2d}".format(x, y, x * y), end=' ')
    print()
print('-' * 50)
