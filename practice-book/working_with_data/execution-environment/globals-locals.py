print globals()

x = 2

print globals()

def f(a, b):
    print locals()

f(1, 2)

def g(a, b=9000):
    print locals()

g('power level')

def h(a, b=9000):
    return '%(a)s is over %(b)d!' % locals()

print h('power level')

