# The computer picks a secret word. The player guesses 
# letters one by one. You need to print the current state
# of the word (e.g., p y _ t h _ _) and track how many lives the player has left.
# later make file for the words rather than a big tuple
import json
import random

with open("words.json", "r") as file:
    category = json.load(file)

print(category["country names"])

def displayWord (guessedList, word):
    for char in word:
        if char not in guessedList:
            print("_", end=" ")
        else:
            print(char, end=" ")
    print()
    
def runGame (word):
    person = [' ', 'O', '\n', '/', '|', '\\', '\n', '/', ' ', '\\']
    parts = [1, 3, 4, 5, 7, 9]
    def remPart (person):
        if parts:
            person[parts.pop()] = ' '

    def displayPerson (person):
        for p in person:
                print(p, end="")
        print()
        
    guessedList = set()

    while not guessedChecked(word, guessedList):
        displayPerson(person)
        displayWord(guessedList, word)
        letter = input("Enter your guess letter: ").lower()
        if letter in word:
            guessedList.add(letter)
        else:
            if parts:
                print("Wrong guess, -1 body part")
                remPart(person)
                displayPerson(person)

                if not parts:
                    print(f"Your are all out of Guesses!, the word was {word}")
                    break
    else:
        print("You guessed correctly, the word was: ")
        displayWord(guessedList, word)

def guessedChecked (word, guessedList):
    for char in word:
        if char not in guessedList:
            return False 
    return True

def pickWord():
    return words[random.randint(0, len(words)-1)]

def chooseTopic ():
    print(
"""What should be the topic for this game?
    Animals (1)
    Country Names (2)
    Programming Related (3)
    Random (4)
""")
    choice = input("Enter here: ")
print("-- Welcome to Hangman Terminal game --")
print("A random word has been chosen, you have 6 attempts to guess it!!")
# startGame(pickWord())