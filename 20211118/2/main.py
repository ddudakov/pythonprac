class Num:
    def __get__(self, obj, objtype=None):
        if hasattr(obj, "_num"): 
            return obj._num
        return 0

    def __set__(self, obj, val):
        if hasattr(val, "real"):
            obj._num = val
        else:
            obj._num = len(val)
            
import sys
exec(sys.stdin.read())
