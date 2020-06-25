"""
Grader Sorter [WIP]
This script sorts grades from highest to lowest from a number of entered grades.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Initializing our grades list
grades = []
# Taking input of grades and storing it in a list
i = 0
print("Enter the grade at the prompt or enter STOP to stop.\n")
while True:
    grade = input("\nEnter the grade(0-100): ")
    i = i+1
    if(type(grade) == str and grade.lower()=="stop"):
        break
    else:
        grades.append(int(grade))
# Printing the values
print(f"\nThe entered grades = {grades}")
print(f"\nThe entered grades sorted from high to low = {grades.sort(reverse=True)}")
print(f"\nShowing top five grades")


    
