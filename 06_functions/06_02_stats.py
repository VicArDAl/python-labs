'''
Write a function stats() that takes in a list of numbers and finds the max, min, average and sum.
Print these values to the console when calling the function.

'''

example_list = [2, 4, 3, 8, 5, 6, 1, 7]
"""example_list = [1, 2, 3, 4, 5, 6, 7]"""""



def stats(example_list):
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

  def sum(example_list):
    total=0
    for i in example_list:
      total+=i
    return total

  def average(example_list):
    am_ele=len(example_list)
    total=sum(example_list)
    media=total/am_ele
    return media

  print(min(example_list))
  print(max(example_list))
  print(sum(example_list))
  print(average(example_list))

  # define the function here
  return

# call the function below here"""
print(stats(example_list))