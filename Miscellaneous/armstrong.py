"""
Armstrong Number
This script checks if a number is an Armstrong number.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Taking input from user, initiazling variables and also checking number of digits in number
number = int(input("Enter a number: "))
armstrongNumber = 0
printNumber = number
numberLength = len(str(number))

# Loop to iterate through each digit, find it's exponent and raise it to the number of digits in the number AND then add it 
while (number > 0):
    digit = number % 10
    armstrongNumber = armstrongNumber + digit**numberLength
    number //= 10

# Conditions to check if a number is Armstrong number
if (armstrongNumber == printNumber):
    print(str(printNumber) + " is an Armstrong number")
else:
    print(str(printNumber) + " is not an Armstrong number")
    