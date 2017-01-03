import time
import resource

def debug(active=True):
    def decorate(func):
        def clocked(*args):
            mem_init = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            t0 = time.time()
            res = func(*args)
            ela = time.time() - t0
            mem_final = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
            mem_diff = mem_final - mem_init
            args = ','.join(map(repr, args))
            print("[{0:.8f} s | {4:,} B | {5:,} B] {1}({2}) -> {3}".format(ela, func.__name__, args, repr(res), mem_diff, mem_final))

            return res

        if active:
            return clocked

        return func

    return decorate
