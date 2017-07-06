class BankAccount:
    def __init__(self):
        self.balance = 0

    def withdraw(self, amount):
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

# inheritance
class MinimumBalanceAccount(BankAccount):
    def __init__(self, minimum_balance):
        BankAccount.__init__(self)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if self.balance - amount < self.minimum_balance:
            print 'Sorry, minimum balance must be maintained.'
        else:
            BankAccount.withdraw(self, amount)

a = BankAccount()
b = BankAccount()

a.deposit(100)
b.deposit(50)
b.withdraw(10)
a.withdraw(10)

print a.balance
print b.balance

aa = MinimumBalanceAccount(30)
aa.deposit(100)
aa.withdraw(80)
aa.withdraw(70)

print aa.balance

class SimpleClass:
    """A simple class"""
    i = 12345
    
    def f(self):
        return 'hello world'

c = SimpleClass()
print c.i
print SimpleClass.i
print c.__doc__
print SimpleClass.__doc__

class Dog:
    kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.tricks = []

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play_dead')

print d.tricks
print e.tricks
print d.kind
print e.kind

# Problem 1
# What will be the output of the following program.

class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()

print a.f(), b.f()
# 'A', 'A'
# wrong: 'A', 'B'
# B.g overrides A.g

print a.g(), b.g()
# 'A', 'B'
