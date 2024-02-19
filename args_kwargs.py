def myfunc(*args):
    return sum(args)

result = myfunc(2,3,4,5,6,7,9)
print(result)

def myfunc(*args):
    return [even for even in args if even % 2 == 0]

result = myfunc(2,3,4,5,6,7,9)
print(result)

def skyline(string):
    result = ''
    
    for index , char in enumerate(string):
        if index % 2 != 0:
            result += char.upper()
        else:
            result += char
    return result
        
    
    

print(skyline('osaretin'))