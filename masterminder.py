import random, sys

#these are 2 lists for testing
answerlist = ["green", "purple", "blue", "pink"]
allcolors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "maroon"]

#this is the main loop that starts the game
def main():
	print ("Welcome to mastermind! Blue is a good color! Git is weird!")
	play = raw_input("Please type yes to begin: ")
	play = play.lower()
	progress = 10;
	if play == "yes":

		print ("The computer has chosen a sequence of four colors for you to guess. These colors are chosen from this list:")
		print (allcolors)
		print ("You have ten tries. ")

		while (progress > 0):
			print (" ")
			print ("please type in 4 colors with spaces in between for your answer list")
			userlist = raw_input("List your stuff: ")
			userlist = userlist.lower()

			if userlist == "quit":
				break


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
			print ("you have"),
			print (progress),
			print ("tries remaining")

			print " "
	else: 
		print "you have failed the game, please run it again."
	print ("The game has ended.")


#this is a small function that checks if two colors are the same thing
def colorMatch(given, answer):
	if given == answer:
		print (given + " is correct")
	else: 
		print (given + " is wrong")


#this method checks if it is in the list
def colorContain(given, list2):
	if not given in allcolors:
		print (given + " is not a valid color!")
	elif not given in list2:
		print (given + " is not in the answer list!")
	else:
		print (given + " is in the list")

def colorTester(list1, list2): #list1 is the user input list, list2 is the answer list
	print ("your answer was:")
	print (list1)
	print (" ")
	for x in range(0, 4):
		print ("we\'re testing position"),
		print (x+1)
		colorMatch(list1[x], list2[x])
		colorContain(list1[x], list2)
		print (" ")


main()

