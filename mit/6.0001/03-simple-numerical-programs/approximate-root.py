import sys

def main(x):
    if x < 0:
        return print('Number must be > 0')
    epsilon = 0.01
    step = epsilon ** 2
    numGuesses = 0
    ans = 0.0
    while abs(ans ** 2 - x) >= epsilon and ans <= x:
        ans += step
        numGuesses += 1
    print('numGuesses = ', numGuesses)
    if abs(ans ** 2 - x) >= epsilon:
        print(ans)
        print('Failed on square root of', x)
    else:
        print(ans, 'is close to square root of', x)

if __name__ == '__main__':
    main(float(sys.argv[1]))
