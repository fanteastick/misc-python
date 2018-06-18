import random, sys

#these are 2 lists for testing

allcolors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "maroon"]

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
		print (allcolors)
		print ("You have ten tries. X: invalid input. C: correct spot and color. Y: color is in the list. N: color is not in the list.")

		while (progress > 0):
			print ("please type in 4 colors with spaces in between for your answer list")
			userlist = raw_input("List your stuff: ")
			userlist = userlist.lower()

			if userlist == "quit":
				break

			userlist = userlist.split(" ")
			listlength = len(userlist)

			print ("X: invalid input. C: correct spot and color. Y: color is in the list. N: color is not in the list.")
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


#this method checks if it is in the list
#X means invalid, C means correct, Y means it's in the list, N means not in list
def colorContain(given, list2, answer):
	if not given in allcolors:
		return "X"
	elif not given in list2:
		return "N"
	elif given == answer:
		return "C"
	else:
		return "Y"

def colorTester(list1, list2): #list1 is the user input list, list2 is the answer list
	print ("your answer was:"),
	print (list1)
	print (" ")
	printer = []
	for x in range(0, 4):
		printer.append(colorContain(list1[x], list2, list2[x]))
	print printer


main()
