'''

Write a script that completes the following tasks.

'''

# define a function that determines<y whether the number is divisible by 4 or 7 and returns a boolean

# define a function that determines whether a number is divisible by both 4 and 7 and returns a boolean

# take in a number from the user between 1 and 1,000,000,000

# call your functions, passing in the user input as the arguments, and set their output equal to new variables 

# print your new variables to display the results
num=int(input("digit a a number between 1 and 1,000,000,000"))


def num_div(num):
    if num%4==0 and num%7==0:
        return True, " it is divisible of 4 and 7"
    if num%4==0:
        return True, " it is divisible of 4"
    if num%7==0:
        return True, " it is divisible of 4"
    else:
        return False



print(num_div(num))






