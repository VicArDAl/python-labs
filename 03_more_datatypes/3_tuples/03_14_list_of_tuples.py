'''
Write a script that takes a string from the user and creates a list of tuples with each word.
For example:

input = "hello world"
result_list = [('h', 'e', 'l', 'l', 'o'), ('w', 'o', 'r', 'l', 'd')]

'''
count=0
result=[]
input="hello world"
result_list=input.split()
size=len(result_list)

while count>size:
    result.append(list(result_list[count]))
    count+=1

#print(result_list)
print(result)
