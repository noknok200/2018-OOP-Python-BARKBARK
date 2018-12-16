import sys


def debugger(func):
    def fun():
        nowname = sys._getframe(1).f_code.co_name + "()"
        caller = sys._getframe(2).f_code.co_name + "()"
        print("{} called by {}".format(nowname, caller))
        return func()
    return fun
