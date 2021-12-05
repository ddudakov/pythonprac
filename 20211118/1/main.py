def objcount(cls):
    cls.counter = 0
    if "__init__" in cls.__dict__:
        cls_init = cls.__init__
    else:
        cls_init = None
        
    if "__del__" in cls.__dict__:
        cls_del = cls.__del__
    else: 
        cls_del = None 
         
    def __init__(self, *args, **kwargs):
        if cls_init: cls_init(self, *args, **kwargs)
        cls.counter += 1
    def __del__(self):
        cls.counter -= 1
        if cls_del: cls_del(self)
    cls.__init__ = __init__
    cls.__del__ = __del__
    return cls

import sys
exec(sys.stdin.read())
