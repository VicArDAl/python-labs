'''
Read in 10 numbers from the user. Place all 10 numbers into an list in the order they were received.
Print out the second number received, followed by the 4th, then the 6th, then the 8th, then the 10th.
Then print out the 9th, 7th, 5th, 3rd, and 1st.

Example input:  1,2,3,4,5,6,7,8,9,10
Example output: 2,4,6,8,10,9,7,5,3,1

'''

list_input=[]
list_output=[]
count=0
count2=1



while count<10:
    number=int(input("Write a number: "))
    list_input.append(number)
    count+=1
count3=(len(list_input))-2
print(count3)

while count2<10:
    list_output.append(list_input[count2])
    count2+=2

while count3>=0:
    list_output.append(list_input[count3])
    count3 -= 2

print(list_output)
