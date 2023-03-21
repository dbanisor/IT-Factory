import functools
from datetime import datetime


# def my_decorator(func):
#     def wrapper():
#         print("before func")
#         func()
#         print("after func")
#     return wrapper
#
# @my_decorator
# def say_hi():
#     print("Hi")
#
# say_hi()

'''
Un decorator care executa functiile decorate doar pe timpul zilei.
'''

def not_during_the_night(func):
    @functools.wraps(func)
    def wrapper():
        if 8 <= datetime.now().hour < 21:
            func()
        else:
            pass
    return wrapper

@not_during_the_night
def say_hello():
    print("Hello")

say_hello()
print(say_hello)