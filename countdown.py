import itertools

target = 123
givens = [100, 10, 2, 3, 5, 2] 
operations = ["+", "+", "+", "+", "+"] # Operations between each number 
correctGuesses = [] # Store correct guesses to print later

# Change integers to floats to avoid integer division errors
for i in range(0,len(givens)):
	givens[i] = float(givens[i])

# Iterate through every possible arrangement of the numbers
for numbers in list(itertools.permutations(givens)):
	# Iterate through all possible combinations of operations
	print(numbers)
	operations = ["+", "+", "+", "+", "+"]
	for j in range(0,4**5):
		# Generate an equation as a string to be evaluated later
		evalString = ""
		for k in range(0,5):
			evalString += str(numbers[k]) + str(operations[k])
		evalString += str(numbers[5])

		# Evaluate string and compare to target
		guess = eval(evalString)
		if guess == target:
			evalString = evalString.replace(".0", "")
			correctGuesses.append(evalString)
		
		# Make next iteration of operations
			
		# Change all end "/"s to "+"s if any are found
		n = 4
		while operations[n] == "/":
			operations[n] = "+"
			n -= 1

		# Change + to -, - to *, and * to /
		if operations[n] == "+":
			operations[n] = "-"

		elif operations[n] == "-":
			operations[n] = "*"

		elif operations[n] == "*":
			operations[n] = "/"

print("\n" + str(len(correctGuesses)) + " ways found:\n")
for i in range(0,len(correctGuesses)):
	print(correctGuesses[i])
