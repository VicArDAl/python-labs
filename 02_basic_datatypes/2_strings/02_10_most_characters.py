'''
Write a script that takes three strings from the user and prints them together with their length.

Example Output:

5, hello
5, world
9, greetings

CHALLENGE: Can you edit to script to print only the string with the most characters? You can look
           into the topic "Conditionals" to solve this challenge.

'''
string1=str(input("Write the first word or sentence"))
string2=str(input("Write the second word or sentence"))
string3=str(input("Write the third word or sentence"))

length1=len(string1)
length2=len(string2)
length3=len(string3)

print("\n",length1,",",string1,"\n",length2,",",string2,"\n",length3,",",string3,"\n")
if length1>length2 and length1>length3:
    print(length1, string1)
if length2>length1 and length2>length3:
    print(length2, string2)
if length3 > length1 and length3 > length2:
    print(length3, string3)