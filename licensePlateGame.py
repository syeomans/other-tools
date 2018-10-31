def incrementOperands(opList):
	"""
	Cycle through list of operations and increment to the next operand in the self.operands list
	"""

	operands = ["+", "-", "/", "*", "**"] # fully editable

	# Start from the end of the list and work backwards
	i = len(opList) - 1

	# If the last operation is the same as the last operand in operands list, increment to the first
	# operand in operands list (repeat over all cases)
	while opList[i] == operands[-1]:
		opList[i] = operands[0]
		i -= 1
	# After setting all the last operands to the first operand, set next operation to the next operand
	opList[i] = operands[operands.index(opList[i])+1]

def incrementNumbers(numList):
	nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

	i = len(numList) - 1
	while numList[i] == nums[-1]:
		numList[i] = nums[0]
		i -= 1

	numList[i] = nums[nums.index(numList[i])+1]

def evaluate(numList, opList):
	evalString = ""
	for i in range(0,3):
		evalString += str(numList[i]) + str(opList[i])
	evalString += str(numList[-1])

	stopCases = ["4**", "5**", "6**", "7**", "8**", "9**"]
	for case in stopCases:
		if case in evalString:
			return(0)

	try:
		return(eval(evalString))
	except ZeroDivisionError:
		return(0)

def getEvalString(numList, opList):
	evalString = ""
	for i in range(0,3):
		evalString += str(numList[i]) + str(opList[i])
	evalString += str(numList[-1])
	return(evalString)

numbers = [0, 0, 0, 0]
operands = ["+", "+", "+"]
hits = 0
idDict = {} # keys are number list ID, values are solutions (if any)

for i in range(0,10000):
	tmpList = numbers[:]
	tmpList.sort()
	numId = ''.join(str(x) for x in tmpList)
	if numId in idDict.keys() and idDict[numId] != "":
		incrementNumbers(numbers)
		continue
	else:
		idDict[numId] = ""

		print(numbers)
		operands = ["+", "+", "+"]

		for j in range(0,5**3-1):
			if evaluate(numbers, operands) == 13:
				print(str(numbers) + " is solvable.")
				print(getEvalString(numbers, operands))
				idDict[numId] = getEvalString(numbers, operands)
				hits += 1
				break
			incrementOperands(operands)
		incrementNumbers(numbers)

ans = float(hits)/len(idDict.keys())
print("Percentage of all license plates that are solvable: " + str(ans))