# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

WORDLIST_FILENAME = "/home/arjun/Documents/Online_Courses/Python_MIT/ps2/words.txt"


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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    right = 0
    wrong = 0
    found = False
    guessed = []
    for j in range(len(letters_guessed)):
        guessed.append(letters_guessed[j].lower())     
    for i in secret_word:
        if i in guessed:
            right = right+1
        else:
            wrong = wrong +1
    if right == len(secret_word):
        found = True
    else:
        found = False
    return(found)
   
def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guessed = []
    for j in range(len(letters_guessed)):
        guessed.append(letters_guessed[j].lower())    
    guess=""
    for i in secret_word:
        if i in guessed:
            guess=guess+i+" "
        else:
            guess=guess+"_ "
    return(guess)
                               
def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters = string.ascii_lowercase
    guessed = []
    for j in range(len(letters_guessed)):
        guessed.append(letters_guessed[j].lower())
    available_letters =""
    for i in letters:
        if i not in guessed:
            available_letters = available_letters+i+" "
    return(available_letters)
        
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
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed=[]
    print("Welcome to the game Hangman!")
    length = len(secret_word)
    print("I am thinking of a word that is",length,"letters long")
    guesses = 6
    warning = 3
    print("You have",guesses,"guesses and",warning,"warnings left.")
    available_letters = get_available_letters(letters_guessed)
    print("Avaiable letters:", available_letters)
    
    vowels =['a','e','i','o','u']
    
    consonants =[]
    for i in string.ascii_lowercase:
        if i not in vowels:
            consonants.append(i)   
    
    found = False
    word=[]
    unique=[]
    for i in secret_word:
        word.append(i)
        for j in word:
            if j not in unique:
                unique.append(j)
                
    while guesses>0:
        guess_letter = input("Please guess a letter:")       
        if str.isalpha(guess_letter) != True:
            warning = warning -1
            if warning < 0:
                guesses = guesses-1
                print("Oops! That is not a letter:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                print("You have 0 warnings remaining &",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
            else:
                print("Oops! That is not a letter, you have",warning," warnings left")
        elif guess_letter in letters_guessed:
            warning = warning -1
            if warning < 0:
                guesses = guesses-1
                print("Oops! You have already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                print("You have 0 warnings remaining &",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
            else:
                print("Oops! You already guessed that letter, you have",warning," warnings left")

        else:
            letters_guessed.append(guess_letter)
            if is_word_guessed(secret_word,letters_guessed) == True:
                found = True
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                break
            elif guess_letter in word:
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                guesses = guesses
                print("You have",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
                    
            else:
                if guess_letter in vowels:
                    guesses = guesses-2
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                    print("---------------------------------")
                    print("You have",guesses,"guesses left (-2 gueses for wrong vowel).")
                    available_letters = get_available_letters(letters_guessed)
                    print("Avaiable letters:", available_letters)
                elif guess_letter in consonants:
                    guesses = guesses-1
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                    print("---------------------------------")
                    print("You have",guesses,"guesses left.")
                    available_letters = get_available_letters(letters_guessed)
                    print("Avaiable letters:", available_letters)
        
    Total_score = guesses*len(unique)
    if found == True:
        print("Conratulations, you Won!!")
        print("Your total score for this game is",Total_score)
    else:
        print("Sorry, you ran out of guesses the word was:",secret_word)
            

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
    my_word_gap = my_word.replace(" ","")
    
    word =[]
    unique=[]
    for i in other_word:
        word.append(i)
        for j in word:
            if j not in unique:
                unique.append(j)
                
    if len(my_word_gap) != len(other_word):
        return(False)
    else:
        n=0
        correct = 0
        wrong = 0
        count = 0
        for i in my_word_gap:
            if i != "_":
                if i.lower() == other_word[n]:
                    correct = correct+1
                else:
                    wrong = wrong +1
            else:
                count=count+1
            n=n+1 
        if count == 1:
            return(False)
        elif correct == len(other_word)-count:
            return(True)
        else: 
            return(False)       
        

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
    matches = False
    word_match = []
    for word in wordlist:
        if match_with_gaps(my_word,word) == True:
            word_match.append(word)
            matches = True
    if matches:
        print(', '.join(word_match))
    else:
        print("No matches found")

#show_possible_matches("t_ _ t")
#show_possible_matches("a_ pl_ ")        
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
    letters_guessed=[]
    print("Welcome to the game Hangman!")
    length = len(secret_word)
    print("I am thinking of a word that is",length,"letters long")
    guesses = 6
    warning = 3
    print("You have",guesses,"guesses and",warning,"warnings left.")
    available_letters = get_available_letters(letters_guessed)
    print("Avaiable letters:", available_letters)
    
    vowels =['a','e','i','o','u']
    
    consonants =[]
    for i in string.ascii_lowercase:
        if i not in vowels:
            consonants.append(i)   
    
    found = False
    word=[]
    unique=[]
    for i in secret_word:
        word.append(i)
        for j in word:
            if j not in unique:
                unique.append(j)
                
    while guesses>0:
        guess_letter = input("Please guess a letter:")  
        if guess_letter == "*":
            show_possible_matches(get_guessed_word(secret_word,letters_guessed))
        
        elif str.isalpha(guess_letter) != True and guess_letter != "*":
            warning = warning -1
            if warning < 0:
                guesses = guesses-1
                print("Oops! That is not a letter:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                print("You have 0 warnings remaining &",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
            else:
                print("Oops! That is not a letter, you have",warning," warnings left")
        
        elif guess_letter in letters_guessed:
            warning = warning -1
            if warning < 0:
                guesses = guesses-1
                print("Oops! You have already guessed that letter:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                print("You have 0 warnings remaining &",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
            else:
                print("Oops! You already guessed that letter, you have",warning," warnings left")

        else:
            letters_guessed.append(guess_letter)
            if is_word_guessed(secret_word,letters_guessed) == True:
                found = True
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                break
            elif guess_letter in word:
                print("Good guess:",get_guessed_word(secret_word,letters_guessed))
                print("---------------------------------")
                guesses = guesses
                print("You have",guesses,"guesses left.")
                available_letters = get_available_letters(letters_guessed)
                print("Avaiable letters:", available_letters)
                    
            else:
                if guess_letter in vowels:
                    guesses = guesses-2
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                    print("---------------------------------")
                    print("You have",guesses,"guesses left (-2 gueses for wrong vowel).")
                    available_letters = get_available_letters(letters_guessed)
                    print("Avaiable letters:", available_letters)
                elif guess_letter in consonants:
                    guesses = guesses-1
                    print("Oops! The letter is not in my word:",get_guessed_word(secret_word,letters_guessed))
                    print("---------------------------------")
                    print("You have",guesses,"guesses left.")
                    available_letters = get_available_letters(letters_guessed)
                    print("Avaiable letters:", available_letters)
        
    Total_score = guesses*len(unique)
    if found == True:
        print("Conratulations, you Won!!")
        print("Your total score for this game is",Total_score)
    else:
        print("Sorry, you ran out of guesses the word was:",secret_word)
            




# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    #pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    #secret_word = choose_word(wordlist)
    #secret_word = "arable"
    #hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    secret_word = choose_word(wordlist)
    hangman_with_hints(secret_word)
