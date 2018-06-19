import random, sys


#subclass
class bcolors:
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PINK = '\033[35m'
    CYAN = '\033[36m'
    GRAY = '\033[37m'
    PURPLE = '\033[45m'

    SRED = '\033[41m'
    SGREEN = '\033[42m'
    SYELLOW = '\033[43m'
    SCYAN = '\033[46m'
    SGRAY = '\033[47m'

    INVALIDGRAY = '\033[107m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    ENDC = '\033[0m'

#this is the list for testing
allcolors = ["red", "green", "yellow", "blue", "pink", "cyan", "gray", "purple", "sred", "sgreen", "syellow", "scyan", "sgray"]

def colorfulPrint(word):
	if word == "red":
		print bcolors.RED + word + bcolors.ENDC ,
	elif word == "green":
		print bcolors.GREEN + word + bcolors.ENDC ,
	elif word == "yellow":
		print bcolors.YELLOW + word + bcolors.ENDC ,
	elif word == "blue":
		print bcolors.BLUE + word + bcolors.ENDC ,
	elif word == "pink":
		print bcolors.PINK + word + bcolors.ENDC ,
	elif word == "cyan":
		print bcolors.CYAN + word + bcolors.ENDC ,
	elif word == "gray":
		print bcolors.GRAY + word + bcolors.ENDC ,
	elif word == "purple":
		print bcolors.PURPLE + word + bcolors.ENDC ,
	elif word == "sred":
		print bcolors.SRED + word + bcolors.ENDC ,
	elif word == "sgreen":
		print bcolors.SGREEN + word + bcolors.ENDC ,
	elif word == "syellow":
		print bcolors.SYELLOW + word + bcolors.ENDC ,
	elif word == "scyan":
		print bcolors.SCYAN + word + bcolors.ENDC ,
	elif word == "sgray":
		print bcolors.SGRAY + word + bcolors.ENDC ,
	else:
		print word,



def getUserList():
	print ("please type in 4 colors with spaces in between for your answer list")
	return raw_input("List your stuff: ")


#this is the main loop that starts the game
def main():
	print ("Welcome to mastermind!")
	play = raw_input("Please type yes to begin: ")
	play = play.lower()
	progress = 10
	random.shuffle(allcolors)
	answerlist = allcolors[0:4]
	random.shuffle(allcolors)
	if play == "yes":
		print (" ")
		print ("The computer has chosen a sequence of four colors for you to guess. These colors are chosen from this list:")
		for c in allcolors:
			colorfulPrint(c)
		print "There are",
		print len(allcolors),
		print "colors."
		print ("**********You need to input the correct colors in the correct order.**********")
		print ("You have ten tries. Type \'key\' for help and \'allcolors\' to see the list again.")

		while (progress > 0):
			userlist = getUserList().lower()

			if userlist == "quit":
				break
			elif userlist == "key":
				getKey()
				continue
			elif userlist == "allcolors":
				for c in allcolors:
					colorfulPrint(c)
				continue

			userlist = userlist.split(" ")
			listlength = len(userlist)

			if userlist == answerlist:
				print "you got the right combination!"
				sys.exit()
			elif not listlength == 4:
				print "you have the wrong number of choices! start over."
				continue

			colorTester(userlist, answerlist)

			progress = progress - 1
			print (" ")
			print ("you have"),
			print (progress),
			print ("tries remaining")

			print " "
	else: 
		print "you have failed the game, please run it again."
	print ("The game has ended.")

def answerColorPrint(condition, color):
	if condition == "invalid":
		print color 
	elif condition == "not in list":
		print bcolors.INVALIDGRAY + color + bcolors.ENDC
	elif condition == "right":
		print bcolors.BOLD + color + bcolors.ENDC
	elif condition == "wrong position":
		print bcolors.UNDERLINE + color + bcolors.ENDC

#this method checks if it is in the list
#X means invalid, C means correct, Y means it's in the list, N means not in list
def colorContain(given, list2, answer):
	if not given in allcolors: # if it's not a color
		answerColorPrint("invalid", given)
	elif not given in list2: # if the color is not in the list
		answerColorPrint("not in list", given)
	elif given == answer: # if the color is on the answer
		answerColorPrint("right", given)
	else: # if the color is in the wrong position
		answerColorPrint("wrong position", given)

def colorTester(list1, list2): #list1 is the user input list, list2 is the answer list
	print ("your answer was:"),
	for color in list1:
		colorfulPrint(color)
	print (" ")
	for x in range(0, 4):
		colorContain(list1[x], list2, list2[x])
	
def getKey():
	print "***** GAME KEY: These colors correspond to the hints given by the game. *****"
	answerColorPrint("invalid", "The word is not a color from the list of possible colors.")
	answerColorPrint("not in list", "The color is not in the answer list.")
	answerColorPrint("wrong position", "You got the right word, wrong position.")
	answerColorPrint("right", "You got the right word in the right position!")
	print ""

main()