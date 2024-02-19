my_string = "osaretin"

# Reverse indexing
print(my_string[-2])

print(len(my_string))


print(my_string[3:])

print(my_string[:3])

print(my_string[2:5])

# ?step size

print(my_string[::1])

# reversing a string with step size
print(my_string[::-1])

print(my_string.capitalize())
print(my_string.upper())
print(my_string.split())

format_string = "Hello {} {} {}"

print(format_string.format('world', 'test', 'python'))

format_string = "Hello {0} {2} {1}"

print(format_string.format('world', 'test', 'python'))

format_string = "Hello {a} {b} {c}"

print(format_string.format(b='world', a='test', c='python'))

# f-strings (string templating in js)
print(f"my name is {my_string}")