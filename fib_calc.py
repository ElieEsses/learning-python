i = True
while i == True:
	amount = input("How many numbers in the Fibinacci Sequence would you like to print? ")
	fib = [0,1]
	count = 0
	line_num = 1

	if amount.isdigit() == True:
		i = False
		amount = int(amount)
		for numbers in range (0,amount - 2):
			fib.append(fib[count] + fib[count +1])
			count += 1

		for digits in fib:
			print("{0}) {1}".format(line_num, digits))
			line_num += 1

		again = input("Would you like to try again? (Y/N) ").upper()
		if again == "Y":
			i = True
		else:
			print("OK. Bye!")
			i = False

	elif amount.isdigit() == False:
		again = input("Sorry but '{0}' is not a number. Would you like to try again? (Y/N) ".format(amount)).upper()
		if again == "Y":
			i = True
		else:
			print("OK. Bye!")
			i = False