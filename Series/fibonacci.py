"""
Fibonacci Series
This script prints Fibonacci series for n value of numbers using variable swap to implement recursion.
@author : MarkisDev
@copyright : https://markis.dev
"""    
number = int(input('Enter the maximum numbers to be displayed: '))

# Initializing our swapping variables and list
a = 0
c = 0
b = 1
seriesList = [0]

# Loop to find the sum of the previous number, append to list and swap the variables to implement recursion
for i in range(1 , number):
    c = a + b
    seriesList.append(c)

# Variable swapping 
    a = b
    b = c 
print("The sequence is as follows: ")
print(seriesList)
