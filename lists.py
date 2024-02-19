students = ['Mike', 'Ada', 'Fedora']

print(students)

print(len(students))

old_students = ['Grace', 'Joan']

all_students = students + old_students

all_students.append('Rhema')
all_students.append('Bola')
all_students.append(2)
print(all_students)

all_students.pop(-1)

all_students.sort(reverse=True)

all_students.reverse()

print(all_students)

numbers = [1,2,3,4,5,6,7]
print(min(numbers))
print(max(numbers))

# comprehension
new_list = [letter for letter in students[0]]
print(new_list)

range_numbers = [num for num in range(1,5)]
print(range_numbers)

range_numbers_2 = [num**2 for num in range(1,5)]
print(range_numbers_2)