import sys


#this method prints the legend of all pieces
def key():
	print ("************LEGEND: THE PIECES*************")
	print ("Uppercase: White; lowercase: black")
	print ("K = king")
	print ("Q = queen")
	print ("B = bishop")
	print ("R = rook")
	print ("N = knight")
	print ("P = pawn")
	print ("Type \'help <letter or name>\' to learn how each piece can move.")


#this method parses the input and returns only the selection that the user makes, either letter or actual word works :) also includes error handling for wrong inputs
def getHelpInput():
	input = raw_input("Type \'help + <letter or name>\' to learn how each piece can move.") #gets user input and saves it
	if not input.startswith("help "):
		print "That was the wrong formatting. Please type again. Make sure there is a space between \'help\' and the name of the piece."
		return False; #wrong formatting means the help message will end
	else:
		returner = input.split(" ") # if it DOES start with help, then it splits the string into a list of 2 strings: help and the word
		returner = returner[1] #change the variable so it only stores the word the user is looking for
		return returner #sends the word to the next method



#this method is the main help command
def help(input): #the input should be a single letter/word
	if input == False: #if the input was wrong then it'll stop the method
		sys.exit()
	def cuteformats(input2): #adding formatting
		print "*****",
		print input.upper(),
		print "*****"

	input = input.lower() #lowercase for error handling


	if input == 'k' or input == "king":
		input = "king"
		cuteformats(input)
		print "The king piece must be protected at all costs. You must move it when the opponent is at a check. It can move in all directions, but only by one square at a time."
		print "If your king cannot move anywhere without being captured, then you have been checkmated, and you lose the game."
	
	elif input == 'q' or input == "queen":
		input = "queen"
		cuteformats(input)
		print "The queen piece is very versatile: it can move along any straight line or diagonal, for any number of spaces."
	
	elif input == 'b' or input == "bishop":
		input = "bishop"
		cuteformats(input)
		print "2 bishops start sitting next to them. Bishops can move along diagonals, for any number of spaces."
	
	elif input == 'r' or input == "rook":
		input = "rook"
		cuteformats(input)
		print "There are 2 rooks that start on the two corners of the board. Rooks can move in straight lines for any number of spaces."
	
	elif input == 'n' or input == "knight":
		input = "knight"
		cuteformats(input)
		print "Two knights start between bishop and rook on both sides. Knights must move two squares in a straight line, then one square along the line perpendicular to the initial direction."
	
	elif input == 'p' or input == "pawn":
		input = "pawn"
		cuteformats(input)
		print "Each side starts with ten pawns. A pawn moves forward one square at a time, except for 2 occasions: "
		print "1. when capturing another piece, the pawn moves diagonally forward by one square. "
		print "2. When moving from its initial position, pawns have the option of moving forward two spaces, instead of one."
	
	else:
		print "That isn't a valid piece. Please check your spelling and try again."


key()
astring = getHelpInput() #make sure to call getHelpInput so the input is the right formatting when you use the help method
help(astring)

