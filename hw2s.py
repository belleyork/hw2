# def createMatrix(rowCount, colCount, dataList) :
#     mat= []
#     for i in range (rowCount):
#         rowList = []
#         for j in range (colCount) :
#             if dataList[j] not in mat:
#                 rowList.append(dataList[j])
#         mat.append(rowList)
#
#     return mat
#
# def substactBase(matr_a, matr_b):
#     # """return matrix that is a result of subtracting two square matrices"""
#     output = []
#     for idx in xrange(len(matr_a)):
#         tmp = []
#         for valA, valB in zip(matr_a[idx], matr_b[idx]):
#             tmp.append(valA - valB)
#         output.append(tmp[:])
#     return output[:]

def matrices():
    a = input('enter first matrices ')
    a = a.split(',')
    b = input('enter second matrices ')
    b = b.split(',')
    c = input('enter third matrices ')
    c = c.split(',')

matrices()

if len(a) == len(b) and len(b) == len(c):
    d=[]
    d.append(a)
    d.append(b)
    d.append(c)

    for row in d:
        for elem in row:
            print(elem, end=' ')
        print()
else:
    print('the quantity of numbers in the matrix should be consistent with other matrices')
    matrices()
