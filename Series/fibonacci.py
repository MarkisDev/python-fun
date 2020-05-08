"""
Fibonacci Series
This script prints Fibonacci series for n value of numbers using variable swap to implement recursion.
@author : MarkisDev
@copyright : https://markis.dev
"""    
n = int(input('Enter the maximum numbers to be displayed: '))
# Initializing our swapping variables and list
a = 0
c = 0
b = 1
l = [0]
for i in range(1 , n):
    c = a + b
    l.append(c)
# Variable swapping 
    a = b
    b = c 
print("The sequence is as follows: ")
print(l)
