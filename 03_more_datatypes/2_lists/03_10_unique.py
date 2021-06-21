'''
Write a script that creates a list of all unique values in a list. For example:

list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
unique_list = [55, 'hi', 4, 13]


'''
unique_list=[]
list_ = [1, 2, 6, 55, 2, 'hi', 4, 6, 1, 13]
for i in list_:
    element=list_.count(i)
    if element==1:
        unique_list.append(i)
print(unique_list)