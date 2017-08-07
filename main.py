from mylibs.memoize import memoize
from mylibs.mapping import mappingClassic
from mylibs.mapping import mapping
from mylibs.filtering import filteringClassic
from mylibs.filtering import filtering
from mylibs.transduce import transduce
from mylibs.push import push
from mylibs.compose import compose
from mylibs.arity import _arity

#
# TESTING: memoize.py
#
print('')
print('')
print('TESTING: memoize.py')

def bitcoin_to_usd(btc):
    return btc * 527


mem_bitcoin_to_usd = memoize(bitcoin_to_usd)

for n in range(1, 10):
    print(mem_bitcoin_to_usd(n))

print('##')
print('It won\'t save any more values')
for n in range(1, 10, 2):
    print(mem_bitcoin_to_usd(n))

#
# TESTING: mapping.py
#
print('')
print('')
print('TESTING: mapping.py')

res = mappingClassic(lambda x: x + 1)([], 1)

print(res)

#
# TESTING: filtering.py
#
print('')
print('')
print('TESTING: filtering.py')

res = filteringClassic(lambda x: x % 2 == 0)([2,4], 7)

print(res)

#
# TESTING: transducer.py
#
print('')
print('')
print('TESTING: transducer.py')

listItems = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

xform = compose(
    mapping(lambda x: x + 1),
    filtering(lambda x: x % 2 == 0)
)

res = transduce( xform, push, [], listItems )

print(res)

# def test_var_args(f_arg, *argv):
#     print "first normal arg:", f_arg
#     for arg in argv:
#         print "another arg through *argv :", arg

# test_var_args('yasoob','python','eggs','test')

    
# var cache = {};
#   return _arity(fn.length, function() {
#     var key = mFn.apply(this, arguments);
#     if (!_has(key, cache)) {
#       cache[key] = fn.apply(this, arguments);
#     }
#     return cache[key];
#   });
    


# name = "Bucky"

# if name is 'Bucky':
#     print('hey bucky')
# elif name is 'lucy':
#     print('hello lucy')
# elif name is 'sammy':
#     print('sup sam?')
# else:
#     print('... who da fuck r you?')

# for f in range(1, 10, 2):
#     print(f)

# incrementIt = 0

# while incrementIt < 10:
#     print(incrementIt)
#     incrementIt += 1
