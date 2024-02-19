for i in ['a', 'b', 'c']:
    try:
        print(i ** 2)
    except TypeError:
        print('An error occurred! Cant perform math operation')

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


try:
  f = open("text.txt", "w")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()
except:
  print("Something went wrong when opening the file")