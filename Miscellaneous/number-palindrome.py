"""
Number Palindrome
This script print checks whether a number is a palindrome or not, without converting it to a string.
@author : MarkisDev
@copyright : https://markis.dev
"""
number = int(input("Enter a number: "))
# Initializing variables
printNumber = number
reversedNumber = 0

# Loop to reverse a number
while(number > 0):
    reminder = number % 10
    reversedNumber = reversedNumber * 10 + reminder
    number = number // 10

# Conditions to check if number is a palindrome
if (reversedNumber == printNumber):
    print(str(printNumber) +" is a palindrome.")
else:
        print(str(printNumber) +" is not a palindrome.")