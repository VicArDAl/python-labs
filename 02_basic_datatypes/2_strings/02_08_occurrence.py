'''
Write a script that takes a string of words and a letter from the user.
Find the index of first occurrence of the letter in the string. For example:

String input: hello world
Letter input: o
Result: 4

'''

string=str(input("Write a script:\n"))
letter=str(input("letter to find:\n"))
print(string.find(letter))
