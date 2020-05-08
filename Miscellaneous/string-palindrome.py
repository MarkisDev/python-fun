"""
String Palindrome
This script print checks whether a string is a Palindrome or not.
@author : MarkisDev
@copyright : https://markis.dev
"""
# Taking input from user and converting it to lower case and trimming whitespaces
word = str(input("Enter a word: ")).lower().strip()
reversedWord = ""

# Finding length of the word
wordLength = len(word)

# Loop to reverse the word
for i in range(wordLength-1,-1,-1):
    reversedWord = reversedWord + word[i]

# Conditions to check if the word is a palindrome
if(word==reversedWord):
    print(reversedWord + " is a Palindrome")
else:
    print(word + " is not Palindrome")

