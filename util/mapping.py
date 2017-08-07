from push import push

def mapping(f):
  return lambda reducing: (
    lambda result, input: (
      reducing(result, f(input))
    )
  )

def mappingClassic(f):
  return lambda result, input: (
    push(result, f(input))
  )