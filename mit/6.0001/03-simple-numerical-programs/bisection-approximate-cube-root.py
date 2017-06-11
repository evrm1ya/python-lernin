import sys

def main(x):
    xIsNegative = x < 0
    if xIsNegative:
        x = x * -1
    epsilon = 0.01
    numGuesses = 0
    low = 0.0
    high = max(1.0, x)
    ans = (high + low) / 2.0
    while abs(ans ** 3 - x) >= epsilon:
        print('low =', low, 'high =', high, 'ans =', ans)
        numGuesses += 1
        if ans ** 3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low) / 2.0
    print('numGuesses =', numGuesses)
    if xIsNegative:
        ans = ans * -1
    print(ans, 'is close to cube root of', x)

if __name__ == '__main__':
    main(float(sys.argv[1]))

