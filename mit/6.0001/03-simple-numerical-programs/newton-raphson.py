import sys

def main(x):
    epsilon = 0.01
    guess = x / 2.0
    numGuesses = 0
    while abs(guess * guess - x) >= epsilon:
        numGuesses += 1
        guess = guess - (((guess ** 2) - x) / (2 * guess))
    print('Square root of', x, 'is about', guess)
    print('Number of guesses:', numGuesses)

if __name__ == '__main__':
    main(float(sys.argv[1]))
