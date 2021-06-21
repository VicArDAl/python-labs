import string
name="I love to work with dictionaries!"


lower=0
upper=0
pun=0
for c in name:
    if c.islower():
         #print (c)
         lower=lower+1

for c in name:
    if c.isupper():
         #print (c)
         upper=upper+1

for c in name:
    if c in string.punctuation:
        pun=pun+1

#print(string.punctuation)
print("Upper case: ", upper)
print("Lower case: ", lower)
print("Punctuation: ", pun)
print("Total chars: ", upper+lower+pun)


