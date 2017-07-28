import math

# Question 1
numList = []
for i in range(2000, 3200):
  if (i % 7 == 0 and i % 5 != 0):
    numList.append(i)
print numList

# Question 2
def factorial(num):
  total = 1
  print num
  for i in range(1, num + 1):
    total = total * i
  print total

factorial(8)

# Question 3
def integral(num):
  output = {}
  for i in range(1, num + 1):
    output[i] = i*i
  print output

integral(5)

# Question 4
def sequence (numbers):
  numbersList = numbers
  numbersTuple = ''
  for i in numbers:
    numbersTuple += str(i) + ", "
  print numbersTuple
  print numbersList


sequence([45,45,6,6,7,88])

# Question 5
class inputOutString():
  def __init__ (self):
    self.str = ''

  def getString(self):
    self.str = raw_input()

  def printString(self):
    print self.str.upper()

newStrObj = inputOutString()
newStrObj.printString()

# Question 6
def retardMath(arr):
  output = []
  for i in arr:
    output.append(math.sqrt((100 * i) / 30))
  print output

retardMath([100,25])

# Question 7
def twoXArray(x,y):
  multiList = []
  row = []
  for i in range(0, x + 1):
    for j in range(0, y +1):
      if len(row) == y + 1:
        multiList.append(row)
        row = []
      else:
        row.append(i * j)
  return multiList

print twoXArray(5,3)

# Question 8