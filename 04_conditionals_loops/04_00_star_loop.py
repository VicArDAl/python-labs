'''

Write a loop that for a number n prints n rows of stars in a triangle shape.

For example if n is 3, you print:

*
**
***

'''

n = 5
count=0
while n >=1:
    n = n-1
    count+=1
    print('*'*count)