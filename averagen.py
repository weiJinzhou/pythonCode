#!/usr/bin/env python3
n = int(input('Please enter the amount of number: '))
sum = 0
count = 0
while count < n:
    number = float(input('NO.{}: '.format(count+1)))
    sum += number
    count += 1
average = sum / n
print('N = {}, Sum = {}'.format(n, sum))
print('Average = {:.2f}'.format(average))
