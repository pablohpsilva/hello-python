def _arity(n, func):
    if n is 0:
        def fun():
            return func(*argv)
        return fun
    elif n is 1:
        def fun(a0):
            return func(*argv)
        return fun
    elif n is 2:
        def fun(a0, a1):
            return func(*argv)
        return fun
    elif n is 3:
        def fun(a0, a1, a2):
            return func(*argv)
        return fun
    elif n is 4:
        def fun(a0, a1, a2, a3):
            return func(*argv)
        return fun
    elif n is 5:
        def fun(a0, a1, a2, a3, a4):
            return func(*argv)
        return fun
    elif n is 6:
        def fun(a0, a1, a2, a3, a4, a5):
            return func(*argv)
        return fun
    else:
        def fun(a0, a1, a2, a3, a4, a5, a6):
            return func(*argv)
        return fun