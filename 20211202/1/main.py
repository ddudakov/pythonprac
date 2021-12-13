from types import FunctionType

def decorator(func, name):
    def wrapper(*args, **kwargs):
        a = (arg for arg in args if type(arg)==int or type(arg)==float or type(arg)==str or type(arg)==bool)
        print(f"{name}: {tuple(a)}, {kwargs}")
        return func(*args,**kwargs)
    wrapper.__name__ = name
    return wrapper

class dump(type):
    def __new__(cls, name, bases, dct):
        newdct={}
        for name, val in dct.items():
            if isinstance(val, FunctionType):
                newdct[name] = decorator(val, name)
            else:
                newdct[name] = val
        return type.__new__(cls, name, bases, newdct)

import sys
exec(sys.stdin.read())
