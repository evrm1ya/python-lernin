import foo
from foo.b import b
from bar.c import c

attrs = dir(foo)

print('attrs\n', attrs)
#print(foo.__builtins__)
print(foo.__name__)
print(foo.__file__)
print(foo.__doc__)
print(foo.__package__)
print(foo.__path__)

b()
c()
