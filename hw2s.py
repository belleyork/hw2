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

a = [[1, 2, 3, 4], [5, 6], [7, 8, 9]]
for row in a:
    for elem in row:
        print(elem, end=' ')
    print()
