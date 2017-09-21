def log(*args, **kw):
    def decorator(f):
        print(*args)
        print('begin call')
        f()
        print('end call')
#        return f
    return decorator

@log()
def f():
    print('no execute')

@log('execute')
def f1():
    print('with execute')


f()
#f1()
