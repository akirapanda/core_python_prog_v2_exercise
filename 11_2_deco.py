#!/usr/bin/env python

from time import ctime, sleep

'deco.py --  无参装饰器示例'

def tsfuns(func):
    def wrapperFunc():
        print '[%s] %s() called' % (
            ctime(), func.__name__
        )
        return func()
    return wrapperFunc

@tsfuns
def foo():
    pass

foo()
sleep(4)

for i in range(2):
    sleep(i)
    foo()