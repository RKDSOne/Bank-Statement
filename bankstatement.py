# bankstatement.py

def main():
	# balance starts at 0
	balance = 0

	# ask user for inputs
	deposit = input("Please enter the amount you'd like to deposit each month: ")
	annualInterest = input("Please enter the annual interest rate (e.g. 0.01): ")
	monthInterest = annualInterest/12
	months = input("Please enter the number of months you will deposit $" + str(deposit) + ": ")

	# calculate the final amount using a for loop
	for newBalance in range(months):
		newBalance = 100 + (balance * (1+monthInterest))
		balance = newBalance

	# output to user
	print("Your monthly deposit is: $" + str(deposit) + ".")
	print("Your annual interest rate is: " + str(annualInterest) + "% per year.")
	print("The number of months you will deposit the amount at this rate is: " + str(months))
	print("Your final amount after " + str(months) + " months will be: " + "%.2f" % round(newBalance,2))
	
main()