def _arity(n, func):
  if n is 1:
    def fun(a0):
      return lambda a0: func(*args)
  elif n is 2:
    def fun(a0, a1):
      return lambda a0, a1: func(*args)
  elif n is 3:
    def fun(a0, a1, a2):
      return lambda a0, a1, a2: func(*args)
  elif n is 4:
    def fun(a0, a1, a2, a3):
      return lambda a0, a1, a2, a3: func(*args)
  elif n is 5:
    def fun(a0, a1, a2, a3, a4):
      return lambda a0, a1, a2, a3, a4: func(*args)
  elif n is 6:
    def fun(a0, a1, a2, a3, a4, a5):
      return lambda a0, a1, a2, a3, a4, a5: func(*args)
  else:
    def fun(a0, a1, a2, a3, a4, a5, a6):
      return lambda a0, a1, a2, a3, a4, a5, a6: func(*args)
