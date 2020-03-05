import random
WORDLIST = [""]
updatedWord = ""
secret = ""
letter = ""
def initialize():
    print "We have a secret word"
    print "_ _ _ _ _"

def getLetter():
    global letter
    letter = str(raw_input('ENTER YOUR GUESS: '))
    print ('YOUR GUESS: ' + letter)

def fillLetter():
    pos = SECRET.find(letter)
    updatedWord[pos] = letter
    
def ifWon():
    if secret == updateWord:
        print ("you win")
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