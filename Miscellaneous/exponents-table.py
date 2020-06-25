"""
Exponents Table
This script prints the exponents table of a desired number.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Taking input of the number from the user
num = float(input("\nEnter the number for which table has to made: "))
print("\n")
# Looping till ten to find the values and printing
for i in range(1, 11):
    product = round(num ** i, 2)
    print(f"{num} ** {i} = {product}")

