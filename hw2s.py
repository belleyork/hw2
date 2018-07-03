num = input('enter amount of matrices you would like to add, subtract, or multiply ')
matricesList = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for x in range(0,int(num)):
  a = input('enter first matrix ')
  a = a.split(',')
  b = input('enter second matrix ')
  b = b.split(',')
  c = input('enter third matricx ')
  c = c.split(',')

  if len(a) == len(b) and len(b) == len(c):
      vars()[matricesList[x]] = []

      vars()[matricesList[x]].append(a)
      vars()[matricesList[x]].append(b)
      vars()[matricesList[x]].append(c)
      print(vars()[matricesList[x]])
  else:
      print('the quantity of numbers in the matrix should be consistent with other matrices')
      exit()
