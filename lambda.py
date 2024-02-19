def square(num):
    return num ** 2

result = list(map(square, [2,3,4,5]))
print(result)

squares = list(map(lambda num: num**2, [2,3,4,5]))
print(squares)

print(list(filter(lambda num : num > 2, (1,2,3,4,6,7))))