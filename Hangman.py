import random
WORDLIST = [""]
updatedWord = ""
secret = ""
letter = ""
def initialize():
    print "We have a secret word"
    print "_ _ _ _ _"
def getLetter():
    print ("Enter a letter")
    global letter
    letter = raw_input()
def ifWon():
    if secret == updateWord:
        print ("you win")
    else:
        getLetter()

def getLetter():
    global letter
    letter = str(raw_input('ENTER YOUR GUESS: '))
    print ('YOUR GUESS: ' + letter)

def fillLetter():
    pos = SECRET.find(letter)
    updatedWord[pos] = letter
    
def ifWon():
    if updatedWord == SECRET:
        print ('You Won!')
    else: 
        getLetter()
        
def main():
    
    initialize()
    getLetter()

def test():
    if (letter in secret):
        pos = secret.find(letter)
        updatedWord[pos] = letter
        print updatedWord.join()
        ifWon()
    else:
        getLetter()