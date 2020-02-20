#!/usr/bin/env python3
def my_decorators(func):
    def wrapper(*args, **kwargs):
        print("Before Call")
        result = func(*args, **kwargs)
        print("After Call")
        return result
    return wrapper

@my_decorators
def add(a, b):
    # 我们的求和函数
    return a + b
