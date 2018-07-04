num = int(
    input('enter amount of matrices you would like to add, subtract, or multiply '))
matricesList = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numList = []
a = [0, 0, 0]
b = [0, 0, 0]
c = [0, 0, 0]

if num < 23 and num > 1:
    for x in range(0, num):
        if len(a) == 3 and len(b) == 3 and len(c) == 3:
            a = input('enter first matrix ')
            a = list(map(float, a.split(',')))
            b = input('enter second matrix ')
            b = list(map(float, b.split(',')))
            c = input('enter third matrix ')
            c = list(map(float, c.split(',')))
        else:
            print('please type in 3 numbers')
            exit()

        if len(a) == len(b) and len(b) == len(c):
            numList.append(matricesList[x])
            vars()[matricesList[x]] = []

            vars()[matricesList[x]].append(a)
            vars()[matricesList[x]].append(b)
            vars()[matricesList[x]].append(c)
        else:
            print(
                'the quantity of numbers in the matrix should be consistent with other matrices')
            exit()
    answer = input(
        'Would you like to add, subtract, or multiply your matrices? ')

    if answer == 'multiply':
        result = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

    if answer == 'add' or answer == 'subtract' or answer == 'multiply':
        for l in range(len(numList)):
            for i in range(len(result)):
                for j in range(len(d[0])):
                    newlist = vars()[numList[l]]
                    if answer == 'add':
                        result[i][j] = result[i][j] + newlist[i][j]
                    if answer == 'subtract':
                        result[i][j] = result[i][j] - newlist[i][j]
                    if answer == 'multiply':
                        result[i][j] = result[i][j] * newlist[i][j]

        for r in result:
            print(r)
    else:
        print('please type "add", "subtract", or "multiply"')
        exit()
else:
    print('please choose an amount less than 27 and greater than 1')
