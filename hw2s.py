num = int(
    input('enter amount of matrices you would like to add, subtract, or multiply '))
matricesList = ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
numList = []

if num < 27:
    for x in range(0, num):
        a = input('enter first matrix ')
        a = list(map(float, a.split(',')))
        b = input('enter second matrix ')
        b = list(map(float, b.split(',')))
        c = input('enter third matricx ')
        c = list(map(float, c.split(',')))

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

    if answer == 'add':
        for i in range(len(d)):
            for j in range(len(d[0])):
                for l in range(len(numList)):
                    print(numList[l])
                    # result[i][j] = result[i][j] + numList[l][i][j]

        print(result)
else:
    print('please choose an amount less than 27')
