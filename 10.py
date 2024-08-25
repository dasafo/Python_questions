# Convert the string "123" into 123, without using the built-api `int()`

def str_to_int(inputStr):
  outputNum = 0
  for char in inputStr:
    for i in range(10):
      if str(i) == char:
        outputNum = outputNum * 10 + i
  return outputNum

print(str_to_int("348"))
