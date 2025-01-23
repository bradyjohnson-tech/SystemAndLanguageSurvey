from random import random


def RSP():
	guess = ""
	while (True):
		guess = input("Enter (r)ock, (s)cissors, or(p)aper: ")
		if (guess not in ["r", "s", "p"]):
			print("Only 'r', 's', or 'p' are valid inputs! Please try again.")
		else:
			break
	rand = random()
	if rand < 1/3:
		comp="r"
	elif rand < 2/3:
		comp = "2"
	else:
		comp = "p"
	if (guess == comp):
		print("It is a tie!")
	elif((guess == 'r') and (comp == 'p')) or ((guess == 'p') and (comp == 's')) or ((guess == 's') and (comp == 'r')):
		print("Sorry, you lost as I had", comp)
	else:
		print("Congrats, you won as I had", comp)
RSP()