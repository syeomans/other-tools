# This script encrypts the user's message with a sliding Cezar cipher. If the user
# has an encoded message, it will decode the message. If not, it will encode a new one.

# The cipher increments the ASCII values of each character of text by an incrementing 
# counter. Due to the maximum readable value of ASCII text being the number 255, the 
# counter will reset at 133.


# Encrypt message with sliding Cezar cipher. Scrambles text by incrementing the ASCII values of the text.
def encode(inStr):
	outStr = ""
	count = 0
	for letter in inStr:
		# Count causes problems if it goes beyond 133. z (ASCII 122) + 133 = 255, the max value of ASCII
		if count >= 133:
			count = -1
		count += 1
		# Increment ASCII value by count
		outStr += chr(ord(letter) + count)
	return outStr

# Decrypt message
def decode(outStr):
	inStr = ""
	count = 0
	for letter in outStr:
		if count >= 133:
			count = -1
		count += 1
		inStr += chr(ord(letter) - count)
	return inStr

# Get user's choice of function and check to make sure it was either "y" or "n"
choice = raw_input("Do you have an encoded message? (y/n) ")
while not(choice == "y" or choice == "n"):
	choice = raw_input("Sorry. I didn't catch that. Do you have an encoded message? (y/n) ")

# If user doesn't have an encoded message, encode their message and write it to a file.
if choice == "n":
	inStr = raw_input("What do you want to say? ")
	outStr = encode(inStr)
	# Open file for writing
	outFile = open("Encoded_message.txt", "w")
	outFile.write(outStr)
	print("Message encoded.")
	print(outStr)
	outFile.close()

# If user has an encoded message, read their message, decode it, and print it. 
if choice == "y":
	inFile = open("Encoded_message.txt", "r")
	inStr = inFile.read()
	inFile.close()
	outStr = decode(inStr)
	print(outStr)