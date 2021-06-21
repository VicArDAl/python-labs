'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''

example_list = [2, 4, 3, 8, 5, 6, 1, 7]


def min(example_list):
   menor = example_list[0]
   for i in example_list:
     if i<menor:
       menor=i
   return (menor)

def max(example_list):
  mayor = example_list[0]
  for i in example_list:
    if i>mayor:
      mayor=i
  return mayor

def resta(max,min):
    total=max-min
    return total
def sum(example_list):
  total=0
  for i in example_list:
    total+=i
  return total


def average(example_list):
  am_ele=len(example_list)
  media=sum(example_list)/am_ele
  return media


print(min(example_list))
print(max(example_list))
print(sum(example_list))
print(resta(max(example_list), min(example_list)))
print(average(example_list))
