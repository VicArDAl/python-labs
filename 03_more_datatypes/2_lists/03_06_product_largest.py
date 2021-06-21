'''
Take in 10 numbers from the user. Place the numbers in a list.
Find the largest number in the list.
Print the results.

CHALLENGE: Calculate the product of all of the numbers in the list.
(you will need to use "looping" - a concept common to list operations
that we haven't looked at yet. See if you can figure it out, otherwise
come back to this task after you have learned about loops)

'''


count =0
list=[]
product=1

while count < 10:
    number=int(input("introduce a number "))
    list.append(number)
    list.sort()
    count+=1

for i in list:
    product*=i


print("the largest number is: ", list[-1])
print("the product of the list is: ", product)
print(list)