class check(type):
    def __new__(cls, nm, bases, dct):
        def check_annotations(self):
            if not hasattr(self, '__annotations__'):
                return True
            try:
                for key, val in self.__annotations__.items():
                        if not isinstance(getattr(self, key), val):
                            return False
                return True
            except Exception:
                return False
        dct['check_annotations'] = check_annotations
        return super().__new__(cls, nm, bases, dct)

import sys
exec(sys.stdin.read())

