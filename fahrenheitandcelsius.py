#!/usr/bin/env python3
e = input('Please tell me what you do:("F": Fahrenheit to Celsius, "C": Celsius to Fahrenheit)')
fahrenheit = 0
celsius = 0
while (e == 'F' or e == 'C') == False:
    e = input('Please tell me what you do:("F": Fahrenheit to Celsius, "C": Celsius to Fahrenheit )')
if e == 'F':
    print('Fahrenheit Celsius')
    while fahrenheit <= 250:
        celsius = (fahrenheit - 32) / 1.8
        print("{:5d} {:7.2f}".format(fahrenheit, celsius))
        fahrenheit += 25
elif e == 'C':
    print('Celsius Fahrenheit')
    while celsius <= 100:
        fahrenheit = celsius * 1.8 + 32
        print("{:5d} {:7.2f}".format(celsius, fahrenheit))
        celsius += 10
