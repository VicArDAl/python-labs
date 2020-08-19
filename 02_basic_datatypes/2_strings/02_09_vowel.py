'''
Write a script that prints the total number of vowels that are used in a user-inputted string.


CHALLENGE: Can you change the script so that it counts the occurrence of each individual vowel
           in the string and print a count for each of them?

'''

script=str(input("Write a script"))
script=script.lower()

long=len(script)
count=0
acount=0
ecount=0
icount=0
ocount=0
ucount=0

while count != long:
    if script[count] == "a":
        acount = acount+1
        #print("acount", acount)
    if script[count] == "e":
        ecount = ecount+1
        #print("ecount", ecount)
    if script[count] == "i":
        icount = icount+1
        #print("icount", icount)
    if script[count] == "o":
        ocount = ocount+1
        #print("ocount", ocount)
    if script[count] == "u":
        ucount = ucount+1
        #print("ucount", ucount)
    count = count + 1
print("\n",script)
print("\na:", acount, "\ne:", ecount, "\ni:", icount, "\no:", ocount, "\nu:", ucount)
print("total vowels: ", acount + ecount + icount + ocount + ucount)








