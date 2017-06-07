# What's the output?
print 2 < 3 and 3 > 1
#=> True
print 2 < 3 or 3 > 1
#=> True
print 2 < 3 or not 3 > 1
#=> True
print 2 < 3 and not 3 > 1
#=> False

# moar
x = 4
y = 5
p = x < y or x < z
print p
#=> True

True, False = False, True
print True, False
#=> False, True
print 2 < 3
#=> True (wrong 1st time - dummy)
# not a big fan of assigning booleans to booleans

# if statment

x = 2
if x == 2:
    print x
else:
    print y

#=> prints 2
# no error since if clause is true

y = 2
if y == 2:
    print y
else:
    x +

# syntax error
