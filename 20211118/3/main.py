from string import ascii_lowercase

class Alpha:
    __slots__ = list(ascii_lowercase)
    def __init__(self, **kwargs):
        for kwr in kwargs:
            setattr(self, kwr, kwargs[kwr])
    def __str__(self):
        ans = ''
        for s in self.__slots__:
            try:
                val = getattr(self, s)
            except:
                pass
            else:
                ans += f'{s}: {val}, '
        if len(ans) > 0:
            return ans[:-2]
        else:
            return ans
class AlphaQ:
    def __init__(self, **kwargs):
        for kwr in kwargs:
            if len(kwr)==1 and kwr >= 'a' and kwr <= 'z':
                setattr(self, kwr, kwargs[kwr])
            else:
                raise AttributeError
    def __str__(self):
        ans = ''
        for d in sorted(self.__dict__):
            val = getattr(self, d)
            ans += f'{d}: {val}, '
        if len(ans) > 0:
            return ans[:-2]
        else:
            return ans
    def __setattr__(self, key, val):
        if len(key)==1 and key >= 'a' and key <= 'z':
            super().__setattr__(key, val)
        else:
            raise AttributeError
import sys
exec(sys.stdin.read())
