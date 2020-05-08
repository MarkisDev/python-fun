"""
Binary Triangle
This script prints a Binary Triangle with inputted number of lines.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Taking input from user for number of lines
number = int(input("Enter the number of lines: "))

# First loop to print number of lines
for i in range(1 , (number+1)):

    # Second loop to print either 0 or 1 depending on the value of i
    for j in range (1 , (i+1)):
        if (j == 1 or j == i):

            # Print 1 or 0 in the same line
            print(1 , end = '')
        else:
            print(0, end = '')

            # Print new line after a part of the triangle is done
    print(end="\n")
    