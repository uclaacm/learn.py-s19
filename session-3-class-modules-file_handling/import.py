#!/usr/bin/python

from example import subtract

print(subtract(4,5.5))

# def introduce_decorator(func):
#     print("Hi!")
#     return func
# 
# def introduce():
#     print("Nice to meet you.")
# 
# introduce = introduce_decorator(introduce)
# introduce()

def introduce_decorator(func):
    def inner(*args, **kwargs):
        print("Hi!")
        func(*args, **kwargs)
    return inner

@introduce_decorator
def introduce(name):
    print("My name is " + name + ". Nice to meet you.")

introduce("Furn")
