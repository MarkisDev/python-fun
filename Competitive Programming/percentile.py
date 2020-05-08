"""
Percentile of a student
This script prints the Percentile of a student.
@author : MarkisDev
@copyright : https://markis.dev
@source : https://www.geeksforgeeks.org/program-to-calculate-percentile-of-a-student-based-on-rank/
""" 
# Taking input from user for student's rank and total number of students who appeared in the exam
rank = int(input("Enter rank of student: "))
number = int(input("Enter number of students who appeared in the exam: "))

# Percentile = (Rank / Total) / Total * 100
percentile = ((number - rank) / number) * 100

# Print Percentile of student after rounding the answer to two decimal places
print("Percentile :" + str(round(percentile,2)) + "%")