from random import *

i = True

while i == True:
	def get_random():
		generated_num = random()

		if generated_num <= .33:
			return "rock"
		elif generated_num <= .66:
			return "paper"
		else:
			return "scissor"

	player = input("Pick one, rock, paper, or scissor. ").lower()
	cpu = get_random()

	print("You picked {0}.".format(player))
	print("The computer picked {0}.".format(cpu))

	if player != "rock" and player != "paper" and player != "scissor":
		print("That's not an option. Try again!")
		player = input("Pick one, rock, paper, or scissor. ")
	else:
		if player == "rock" and cpu == "scissor":
			print("You win!")
			i = False
		elif player == "paper" and cpu == "rock":
			print("You win!")
			i = False
		elif player == "scissor" and cpu == "paper":
			print("You win!")
			i = False
		elif player == cpu:
			print("Tie game")
			i = False
		else:
			print("You lose.")
			i = False

	again = input("Would you like to play again? (Y/N) ").lower()

	if again == "y":
		i = True
	if again == "n":
		print("Ok. Thanks for playing!")