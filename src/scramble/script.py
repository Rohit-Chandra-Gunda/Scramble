

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """

    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()

    return wordlist

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    word = word.lower()
    score = 0
    for x in word:
        score += SCRABBLE_LETTER_VALUES[x]
    score *= len(word)
    if len(word) is n:
        score += 50
    return score





def displayHand(hand):
    """
    Displays the letters currently in the hand.


    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       # print all on the same line
    print()                             # print an empty line



def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    hand2 = {}
    for x in hand.keys():
        hand2[x] = hand[x]
    for x in word:
        hand2[x] = hand2.get(x, 0) - 1
    return hand2




def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    if len(word) is 0:
        return False
    freq = getFrequencyDict(word)
    for x in freq:
        if hand.get(x, 0) < freq.get(x, 0):
            return False
    if word in wordList:
        return True
    else:
        return False





def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())



def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand,:



      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    total = 0
    while calculateHandlen(hand) > 0:
        print("Current Hand: ", end="")
        displayHand(hand)
        word = input('Enter word, or a "." to indicate that you are finished: ')
        if word is ".":
            print("Goodbye!", end=" ")
            break
        if isValidWord(word, hand, wordList):
            score = getWordScore(word, n)
            total += score
            hand = updateHand(hand, word)
            print('"' + word + '" ' + 'earned ' + str(score) + ' points. Total: ' + str(total) + ' points')
            if not calculateHandlen(hand) > 0:
                print("Run out of letters.", end=" ")
                break
        else:
            print("Invalid word, please try again.")
    print("Total score: " + str(total) + " points.")





def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.


    """
    options = ["n", "r", "e"]
    hand = {}
    c = "n"
    while c[0] is not "e":
        c = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        c = c.lower()
        if c[0] not in options or len(c) is not 1:
            print("Invalid command.")
            continue
        elif c[0] is options[1] and len(hand) is 0:
            print("You have not played a hand yet. Please play a new hand first!")
            continue
        elif c[0] is "e":
            break
        if c[0] is options[0]:
            hand = dealHand(HAND_SIZE)
        hand2 = {}
        for x in hand.keys():
            hand2[x] = hand[x]
        playHand(hand2, wordList, HAND_SIZE)
    print("Thank you for playing the game.^^.Please come again later.")



if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
