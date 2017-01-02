import time

def debug(active=True):
    def decorate(func):
        def clocked(*args):
            t0 = time.perf_counter()
            res = func(*args)
            ela = time.perf_counter() - t0
            args = ','.join(map(repr, args))
            print("[{0:.8f}s] {1}({2}) -> {3}".format(ela, func.__name__, args, repr(res)))
            return res

        if active:
            return clocked

        return func

    return decorate
