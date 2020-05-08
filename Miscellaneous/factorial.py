"""
Factorial
This script prints the factorial of an entered number.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Taking input from user and initializing factorial variable
number = int(input("Enter a number: "))
factorial = 1

# Loop to multiply consecutive numbers and store them to factorial variable
for i in range(1 , (number + 1)):
    factorial =  factorial * i

# Printing the output
print("Factorial of " + str(number) + " : " + str(factorial))
