num = input('enter amount of matrices you would like to add, subtract, or multiply ')
matricesList = ['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
a=[]
b=[]
c=[]

def matrices():
    a = input('enter first matrix ')
    a = a.split(',')
    b = input('enter second matrix ')
    b = b.split(',')
    c = input('enter third matricx ')
    c = c.split(',')

for x in range(1,int(num)+1):
  matrices()
  for x in range(0, int(num)):
      if len(a) == len(b) and len(b) == len(c):
          matricesList[x]=[]
          matricesList[x].append(a)
          matricesList[x].append(b)
          matricesList[x].append(c)

          print(d)
          print(e)
          print(f)

#
#     for row in d:
#         for elem in row:
#             print(elem, end=' ')
#         print()
# else:
#     print('the quantity of numbers in the matrix should be consistent with other matrices')
#     matrices()
