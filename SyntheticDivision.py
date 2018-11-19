"""This script performs synthetic division on a list of coefficients as the dividend
by an integer as the divisor. If user instead enters two string arguments (for example, 
x^2+4x+4 and x+2), the strings will be formatted into a list and integer respectively.
Output can be either a string (pass an outOption of "s") or a list of coefficients 
(selected by default)."""

#Generates a list of coefficients from a string
def coefList(instr):
	alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
	newstr = ""
	for char in instr:
		#replace all letters with "x"
		if char in alphabet:
			newstr += "x"
		#add delimiting space before each sign
		elif char == "+"or char == "-":
			newstr += " " + char
		else:
			newstr += char
	#add a leading 1  and + where necessary
	if newstr[1] != "-":
		newstr = "+" + newstr
	newstr = newstr.replace("+x","+1x")
	newstr = newstr.replace("-x","-1x")
	newstr = newstr[1:] #ended up with leading space. had to remove
	#change input string (now newstr) into list
	inlist = newstr.split(" ")
	#format list by explicitly adding x^1 and x^0
	i = 0
	for term in inlist:
		if term[-1] == "x":
			inlist[i] = term + "^1"
		if "x" not in term:
			inlist[i] = term + "x^0"
		i += 1
	#generate list of coefficients
	coefList = []
	#create n elements and fill with a default 0 for each term
	for i in range(0,int(inlist[0][-1])+1):
		coefList.append(0)
	#fill in values for each term that is non-zero
	i=0
	for coef in inlist:
		nums = inlist[i].split("x^")
		coefList[int(nums[1])] = eval(nums[0])
		i += 1
	coefList.reverse() #list is backwards; put it forwards
	return(coefList)


def synthDiv(dividend,divisor,outOption = "l"):
	#if user entered a string, format string into a list of coefficients, and run function as a list
	if type(dividend) is str and type(divisor) is str:
		clist = coefList(dividend)

		#format divisor string into an integer with reversed sign
		if "+" in divisor:
			divisorSplit = divisor.split("+")
			divisorInt = int(divisorSplit[1])
		elif "-" in divisor:
			divisorSplit = divisor.split("-")
			divisorInt = 0-int(divisorSplit[1])
		#now that the user's strings are formatted, feed that info back in
		return(synthDiv(clist,divisorInt,outOption))

	#if user entered a list of coefficients and an integer, perform synthetic division with those coefficients
	elif type(dividend) is list and type(divisor) is int or type(divisor) is float and type(dividend) is list:
		divisor = float(divisor)
		quotient = []
		for element in dividend:
			quotient.append(0)
		quotient[0] = float(dividend[0])
		for i in range(1,len(dividend)):
			quotient[i] = round(dividend[i] - quotient[i-1]*divisor,2)

		#format output either as a list or string, depending on user's choice of option (outOpt)
		#if user chose list (default), no further work necessary
		if outOption == "l":
			return(quotient)
		#if user chose string, format output in equation form (add in x's and etc)
		elif outOption == "s":
			outStr = ""
			#loop through each coefficient in quotient list
			i = 0
			for coef in quotient:
				#if the coefficient is 0, skip
				if coef == 0:
					continue
				#if counter is on last element in quotient list, format as remainder
				elif i == len(quotient)-1:
					outStr += ", rem: " + str(coef)
				#if coefficient is 1, add x^i without leading coefficient
				elif coef == 1:
					outStr += "+x^" + str(len(quotient)-2-i)
				#if coefficient is -1, add x^i without leading coefficient
				elif coef == -1:
					outStr += "-x^" + str(len(quotient)-2-i)
				#if coefficient is positive, add x^i with leading coefficient and sign
				elif coef >0:
					outStr += "+" + str(coef) + "x^" + str(len(quotient)-2-i)
				#if coefficient is negative, add x^i with leading coefficient and sign
				else:
					outStr += str(coef) + "x^" + str(len(quotient)-2-i)
				i += 1
			#remove x^1, x^0, .0, and leading sign if positive
			outStr = outStr.replace("x^1","x")
			outStr = outStr.replace("x^0","")
			outStr = outStr.replace(".00","")
			outStr = outStr.replace(".0","")
			if outStr[0] == "+":
				outStr = outStr[1:]
			return(outStr)
		else:
			return("Invalid option")

	#if user entered an invalid format, return error
	else:
		return("Invalid format")


#Finds all factors of a given number
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

#Finds all real roots of a given polynomial or list of coefficients
def realRoots(inlist):
	#if user entered a polynomial, format as a list of coefficients and run again as a list
	if type(inlist) is str:
		return(realRoots(coefList(inlist)))

	#If user entered a list of coefficients, find all combinations of (factors of p) / (factors of q). 
	#Then test if each p/q is a factor using synthetic division. P is the leading coefficient,
	#and q is the trailing coefficient.
	elif type(inlist) is list:
		outlist = []
		p = inlist[-1]	#p is the leading coefficient
		q = inlist[0]	#q is the trailing coefficient
		#find all factors of p and q
		pfactors = list(factors(p))
		qfactors = list(factors(q))
		pq = []	#list of all p/q values
		#for each possible p/q, add p/q and its negative in lowest terms to the list unless it's there already
		for p in pfactors:
			for q in qfactors:
				el = float(p)/float(q)
				if el not in pq:
					pq.append(el)
					pq.append(0 - el)
		#Test each p/q using synthetic division to see if it is a factor. If the remainder is 0, it is a factor.
		for el in pq:
			testIfFactor = synthDiv(inlist,el)
			if testIfFactor[-1] == 0:	#testIfFactor[-1] is the remainder of the synthetic division
				outlist.append(0-el)
		return(outlist)

	#if user did not enter a valid format, throw error
	else:
		return("Invalid format")

#Test script
# print synthDiv([1,4,4],2,"l")
# print synthDiv([1,4,4],2,"s")
# print synthDiv("x^2+4x+4","x+2","l")
# print synthDiv("x^2+4x+4","x+2","s")
# print()
# print realRoots([1,4,4])
# print realRoots("x^2+4x+4")