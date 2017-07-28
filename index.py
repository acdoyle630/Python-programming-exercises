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
def wordSort(string):
  stringArray = string.split(',')
  stringArray.sort()
  print stringArray

wordSort('hello,how,are,you')

# Question 9
def cap(words):
  return words.upper()

print cap('fuck you')

#Question 10
def sortDuplicateCheck (words):
  wordArray = words.split(' ')
  print wordArray
  my_list = []
  for i in wordArray:
    print i
    if i in my_list:
      print 'duplicate'
    else:
      my_list.append(i)
  return my_list



print sortDuplicateCheck('hello hello hello hi this is a test test')

#Question 11
def numberDivByFive(numberString):
  numberArray = numberString.split(',')
  numbersByFive = []
  for i in numberArray:
    if int(i) % 5 == 0:
      numbersByFive.append(int(i))
  return numbersByFive

print numberDivByFive('1,2,3,4,5,6,7,8,10,15')


numberDivByFive('10,13,14,15')

#Question 12
for i in range (1000, 3001):
  evenNumbers = []
  if i % 2 == 0:
    evenNumbers.append(i)

#Question 13
def letterNumCount(string):
  result = {'DIGITS': 0, 'LETTERS': 0}
  for i in string:
    if i.isdigit():
      result['DIGITS'] += 1
    if i.isalpha():
      result['LETTERS'] += 1
  print result

letterNumCount('asdf234jkhyiuy7869876ghguy   lkjhuio9999lkjlj')

#Question 14
def upperVsLower(string):
  result= {"UPPER": 0, "LOWER": 0}
  for i in string:
    if i.isupper():
      result["UPPER"] += 1
    if i.islower():
      result["LOWER"] += 1
  return result

print upperVsLower('ADKLJHLKJHjklhkjlhlkjHKLJHDDJ908097KIOUI')
