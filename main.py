enteredString = input('Enter a pattern - Please enter in CAPITAL LETTERS ONLY:   ')
error = 'False'

if ('A' in enteredString) == True:
  replacedString = enteredString.replace('T', 'U')
else:
  error = 'True'

if ('T' in enteredString) == True:
  replacedString = enteredString.replace('T', 'U')
else:
  error = 'True'

if ('G' in enteredString) == True:
  replacedString = enteredString.replace('T', 'U')
else:
  error = 'True'

if ('C' in enteredString) == True:
  replacedString = enteredString.replace('T', 'U')
else:
  error = 'True'

if (' ' in enteredString):
  error = 'True'


if error == 'True':
  print('There is an erorr in the input')
  

if error == 'False':
  print(replacedString)



