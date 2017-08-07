def memoize(func):
    cache = {}    
    def mem(arg):
        if (not(arg in cache.keys())):
            print('saving new value')
            cache[arg] = func(arg)
        return cache.get(arg)
    return mem