def collatz(number):
	return number//2 if number%2 == 0 else number*3+1

try:
	inputNum = int(input())
	while inputNum != 1:
		print(collatz(inputNum))
		inputNum = collatz(inputNum)

except ValueError:
	print("Error: Please Enter An Integer.")
