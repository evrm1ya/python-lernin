# bank account

# okay for just one account
balance = 0

def deposit(amount):
    global balance
    balance += amount
    return balance

def withdraw(amount):
    global balance
    balance -= amount
    return balance

# local state
def make_account():
    return {'balance': 0}

def deposit(account, amount):
    account['balance'] += amount
    return account['balance']

def withdraw(account, amount):
    account['balance'] -= amount
    return account['balance']

a = make_account()
b = make_account()

deposit(a, 100)
deposit(b, 50)
withdraw(b, 10)
withdraw(a, 10)

print a
print b

