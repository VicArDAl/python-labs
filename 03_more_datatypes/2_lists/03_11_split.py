'''
Write a script that takes in a string from the user. Using the split() method,
create a list of all the words in the string and print the word with the most
occurrences.

'''

script=str(input("type a script please: "))
script_split=script.split()
print(script_split)
bigger_amount=0
solution=[]


for i in script_split:
    amount=script_split.count(i)
    if amount>=bigger_amount:

        bigger_amount=amount
        palabra=i

    print(i)
    print(amount)
print("solucion")
print(palabra,bigger_amount)