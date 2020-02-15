#!/usr/bin/env python3
row = int(input("Enter the number of rows: "))
print('=' * 50)
# part 1
a = row
while a > 0:
    print('*' * a)
    a -= 1
print('-' * 50)
# part 2
for i in range(1, row + 1):
    print('*' * i)
print('-' * 50)
# part 3
n = row
while n > 0:
    print(' ' * (row - n), '*' * n)
    n -= 1
print('=' * 50)
