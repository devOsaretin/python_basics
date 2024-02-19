list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
list3 = ['x', 'y', 'z']

zipped = zip(list1, list2, list3)

for item in zipped:
  print(list(item))

  # convert a tuple to a list
list(zipped)