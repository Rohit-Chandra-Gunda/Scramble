from script import *
import time

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
#
#
# Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """


    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    bestScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for word in wordList:
        # If you can construct the word from your hand
        if isValidWord(word, hand, wordList):
            # find out how much making that word is worth
            score = getWordScore(word, n)
            # If the score for that word is higher than your best score
            if (score > bestScore):
                # update your best score, and best word accordingly
                bestScore = score
                bestWord = word
    # return the best word you found.
    return bestWord

#
# Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # Keep track of the total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while (calculateHandlen(hand) > 0) :
        # Display the hand
        print("Current Hand: ", end=' ')
        displayHand(hand)
        # computer's word
        word = compChooseWord(hand, wordList, n)
        # If the input is a single period:
        if word == None:
            # End the game (break out of the loop)
            break
            
        # Otherwise (the input is not a single period):
        else :
            # If the word is not valid:
            if (not isValidWord(word, hand, wordList)) :
                break
            # Otherwise (the word is valid):
            else :
                # Tell the user how many points the word earned, and the updated total score 
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')              
                # Update hand and show the updated hand to the user
                hand = updateHand(hand, word)
                print()
    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    print('Total score: ' + str(totalScore) + ' points.')

    
#
# Problem #6: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.


    wordList: list (string)
    """
    print("The scores given for the letters are .")
    print("[",end=" ")
    for x in SCRABBLE_LETTER_VALUES:
        print("( "+x+" = "+str(SCRABBLE_LETTER_VALUES[x])+" )",end=" ")
    print(" ]")
    print("The scores of individual letters are added and the sum is multiplied by length of the word.")
    print("If all the letters are used in first try, you get 50 bonus points!")
    print("The game starts now! Good luck!")
    options = ["n", "r", "e"]
    options2 = ["c", "u"]
    hand = {}
    c = "n"
    while c[0] is not "e":
        c = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        c = c.lower()
        if c[0] is "e":
            break
        if c[0] not in options or len(c) is not 1:
            print("Invalid command.")
            continue
        elif c[0] is options[1] and len(hand) is 0:
            print("You have not played a hand yet. Please play a new hand first!")
            continue
        if c[0] is options[0]:
            hands = 0
            while not hands > 0:
                hands = int(input("Enter the size of the hand. (more than 0)"))
                if not hands > 0:
                    print("Invalid number.")
            HAND_SIZE = hands
            hand = dealHand(HAND_SIZE)
        hand2 = {}
        for x in hand.keys():
            hand2[x] = hand[x]
        while c[0] not in options2 or len(c) is not 1:
            c = input("Enter u to have yourself play, c to have the computer play: ")
            if c[0] not in options2 or len(c) is not 1:
                print("Invalid command.")
        if c[0] is "u":
            playHand(hand2, wordList, HAND_SIZE)
        else:
            compPlayHand(hand2, wordList, HAND_SIZE)
    print("Thank you for playing the game.^^.Please come again later.")


if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


