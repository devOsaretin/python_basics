numbers = [1,2,3,4,5,6,7]

for number in numbers:
    print(number)


x = 0
while x < 5:
    print(x)
    x += 1

#enumerate generates an index along side the iterable's value
for index, value in enumerate(numbers):
    print([index, value])
for y in enumerate(numbers):
    print(y)


for i in range(10):
    print(i)

