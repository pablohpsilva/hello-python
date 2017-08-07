import functools

def transduce(xform, reducing, initial, input):
  return functools.reduce(xform(reducing), input, initial)
