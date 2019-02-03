import random

number = random.randrange(1, 50)
guess = input("the computer has chosen a number from 1-50. Take a guess what it was. ")

i = True

while i == True:
	if int(guess) == number:
		print("You win!")
		number = random.randrange(1, 50)
		i = False
		again = input("Play again? (Y/N)")
		if again.upper() == "Y":
			i = True
			guess = input("the computer has chosen a number from 1-50. Take a guess what it was. ")
		elif again.upper() == "N":
			print("OK. Good Game!")
	elif int(guess) > number:
		guess = input("Lower. Try again. ")
	elif int(guess) < number:
		guess = input("Higher. Try again. ")