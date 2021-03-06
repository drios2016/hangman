from random import randint
import time
  
def takeBreak(sec):
	for i in range(0,sec):
		print "..."
		time.sleep(1)
    
def chooseWord():
	num = 0
	file = open("words.txt", "r")
	num = file.readlines()
	word = num[randint(0,len(num)-1)]
	file.close()
	return word
  
def printFig(letters):
	lString = ''
	for i in range (0, len(letters)):
		lString = lString + letters[i]
	print lString
    
def goodGuess(guess, word, letters):
	for i in range(0, len(word)):
		if word[i] == guess:
			letters[i] = guess + ' '
	return letters
  
def guessWord(word, chances):
	print "Would you like to guess the word? Y/N"
	ans = input()
	if (ans == 'Y'):
		print "What's your guess?"
		wGuess = input()
			if (wGuess == word):
				print "You got it!"
				return True, chances
			else:
				chances = chances - 1
				print "Nope, nice try! You have ", chances, " chances left!"
				return False, chances
	else:
		print "Okay!"
		return False, chances

def blanks(word):
	letters = []
	for i in range (0, len(word)):
		letters.append("_ ")
	return letters
  
def play():
	word = chooseWord()
	letters = blanks(word)
    print "Kay! I've chosen a word! It has ", len(word), " letters!"
    print "You have 7 chances! Let's play!" 

	win = False
	chances = 7
	while(chances > 0 and '_ ' in letters and win == False):
		printFig(letters)
		print "Guess a letter!"
		guess = input()
		if (guess in word):
			print "Correct!"
			letters = goodGuess(guess, word, letters)
			win, chances = guessWord(word, chances)
		else:
			chances = chances - 1
			print "Oooh, sorry! You have ", chances, " chances left!"
			win, chances = guessWord(word, chances)
  
	if ('_ ' not in letters or win == True):
		print "You won! The word was: ", word
	elif (chances == 0):
		print "Boo...maybe next time? The word was: ", word

#####MAIN#####
while (1):
  print "Would you like to play hangman? Y/N"
  ans = input()
  if (ans == 'Y'):
    play()
  elif (ans == 'N'):
    print ("Aw, kay.")
    takeBreak(randint(1,5))
  else:
    print ("That's invalid input!")
