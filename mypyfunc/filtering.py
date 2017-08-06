from push import push

def filtering(predicate):
  return lambda reducing: (
    lambda result, input: (
      reducing(result, input) if predicate(input) else result
    )
  )

def filteringClassic(predicate):
  return lambda result, input: (
    push(result, input) if predicate(input) else result
  )
