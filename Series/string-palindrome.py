"""
String Palindrome
This script print checks whether a string is a palindrome or not.
@author : MarkisDev
@copyright : https://markis.dev
"""
s = str(input("Enter a word: ")).lower().strip()
ns = ""
l = len(s)
for i in range(l-1,-1,-1):
    ns = ns + s[i]
if(s==ns):
    print(ns + " is a palindrome")
else:
    print(s + " is not palindrome")

