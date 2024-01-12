num=int(input("enter a number"))
def printValue(digit):

	
	if digit == '0':
		print("Zero ", end = " ")

	
	elif digit == '1':
		print("One ", end = " ")

	elif digit == '2':
		print("Two ", end = " ")

	
	elif digit=='3':
		print("Three",end=" ")

	
	elif digit == '4':
		print("Four ", end = " ")

	
	elif digit == '5':
		print("Five ", end = " ")

	
	elif digit == '6':
		print("Six ", end = " ")

	
	elif digit == '7':
		print("Seven", end = " ")

	elif digit == '8':
		print("Eight", end = " ")


	elif digit == '9':
		print("Nine ", end = " ")


def printWord(N):
	i = 0
	length = len(N)

	
	while i < length:
		
		
		printValue(N[i])
		i += 1
N = "123"
printWord(N)

