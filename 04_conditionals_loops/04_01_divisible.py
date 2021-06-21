'''
Write a program that takes a number between 1 and 1,000,000,000
from the user and determines whether it is divisible by 3 using an if statement.
Print the result.

'''
num=0
num=int(input('Write a number between 1 and 1,000,000,000: '))
divisible=num%3

if divisible == 0:
    print('The number',num,'is divisible by 3')

else:
    print('The number ',num,'is not divisible by 3')
