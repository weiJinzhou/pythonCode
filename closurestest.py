#!/usr/bin/env python
def add_number(num):
    def adder(number):
        # 这是一个闭包
        return num + number
    return adder
