#!/usr/bin/python
# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# TODO: Need to add Hangman with Hints

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    for char in secret_word:
        if char not in letters_guessed:
            return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    result = ''
    for char in secret_word:
        if char in letters_guessed:
            result += char + ' '
            continue
        result += '_ '
    return result

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    if len(letters_guessed) == 0:
        return string.ascii_lowercase
    letters_joined = ''.join(letters_guessed)
    return re.sub('([' + letters_joined + '])', '', string.ascii_lowercase) 

vowels = ['a', 'e', 'i', 'o', 'u']

def guesses_to_decrement(guess):
    if guess in vowels:
        return 2
    return 1

def total_score(secret_word, guesses):
    '''
    Returns the number of unique characters in secret_word *
    remaining guesses.
    '''
    return len({c for c in secret_word}) * guesses
    
def print_horizontal_line():
    print('-------------')

def print_loser_message(secret_word):
    print('You lose.')
    print('Secret word: %s' % secret_word)

def print_round_stats(warnings, guesses, letters_guessed):
    print_horizontal_line()
    print('You have %d warnings left.' % warnings)
    print('You have %d guesses left.' % guesses)
    print('Available letters: %s' % get_available_letters(letters_guessed))

def print_round_results(word, guesses, warnings, letters_guessed, result):
    guessed_word = get_guessed_word(word, letters_guessed)
    if result == 'not_valid':
        print('Oops! That is not a valid letter.')
        print('You have %d warnings left: %s' % (warnings, guessed_word))
    elif result == 'already_guessed':
        print("Oops! You've already guessed that letter.")
        print('You have %d warnings left: %s' % (warnings, guessed_word))
    elif result == 'not_found':
        print('Oops! That letter is not in my word: %s' % guessed_word)
    elif result == 'good_guess':
        print('Good guess: %s' % guessed_word)
    elif result == 'success':
        print_horizontal_line()
        print('Congratulations, you won!')
        print('The word is: %s' % word)
        print('Your total score for this game is: '
                + '%d' % total_score(word, guesses))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    word_length = len(secret_word)
    guesses = 6
    warnings = 3
    letters_guessed = []
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is %d letters long.' % word_length)

    while guesses > 0:
        print_round_stats(warnings, guesses, letters_guessed)
        guess = str(input('Please guess a letter: ')).lower()
        result = ''
        
        if guess == 'quit':
            break

        if not str.isalpha(guess) or not len(guess) == 1:
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print_round_results(secret_word, guesses, warnings,
                    letters_guessed, 'not_valid')
            continue

        if guess in letters_guessed:
            if warnings > 0:
                warnings -= 1
            else:
                guesses -= 1
            print_round_results(secret_word, guesses, warnings,
                    letters_guessed, 'already_guessed')
            continue
        
        letters_guessed.append(guess)

        if is_word_guessed(secret_word, letters_guessed):
            print_round_results(secret_word, guesses, warnings,
                    letters_guessed, 'success')
            break
        elif guess in secret_word:
            print_round_results(secret_word, guesses, warnings,
                    letters_guessed, 'good_guess')
        else:
            guesses -= guesses_to_decrement(guess)
            print_round_results(secret_word, guesses, warnings,
                    letters_guessed, 'not_found')
    else:
        print('You ran out of guesses.')
        print('The word is %s' % secret_word)

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    pass



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    #hangman('apple')
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
