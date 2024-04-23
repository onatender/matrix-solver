import numpy as np

np.set_printoptions(precision=3, suppress=True,linewidth=150)

def yer_degistir(matrix, row1, row2):
    if row1 == row2:
        return matrix
    print(f"Satır {row1} ve Satır {row2} yer değiştiriliyor.")
    row1 -= 1
    row2 -= 1
    for index, item in enumerate(matrix[row1]):
        temp = matrix[row2][index]
        matrix[row2][index] = item
        matrix[row1][index] = temp
    return matrix

degiskenler = [3, -2, 4, 5, 1, 7, 6, 3, 2, 1]

matrix1 = np.array([    
[-6 ,-6 ,7 ,1 ,-140],
[-8 ,-8 ,8 ,6 ,-200],
[2 ,9 ,7 ,-2 ,86],
[9 ,7 ,-8 ,1 ,170]
],
dtype=float
)


print(matrix1)

for i in range(len(matrix1) - 1):
    enbuyuk = matrix1[:, i][i:][0]
    enbuyukindex = 0 + i
    for index, content in enumerate(matrix1[:, i][i:]):
        if abs(content) > abs(enbuyuk):
            enbuyukindex = index + i
            enbuyuk = content
    yer_degistir(matrix1, i + 1, enbuyukindex + 1)

print(matrix1)


print("Üst üçgensel hale getiriliyor...")
for col in range(len(matrix1) - 1):
    for row in range(len(matrix1) - 1 - col):
        matrix1[row + 1 + col] -= (
            matrix1[row + 1 + col][col] / matrix1[col][col]
        ) * matrix1[col]

matrix1 = np.around(matrix1, decimals=10)
print(matrix1)

def pivot(row):
    for item in row:
        if item != 0:
            return item


print("Pivotlara bölünüyor...")
for index, row in enumerate(matrix1):
    matrix1[index] /= pivot(row)

print(matrix1)

print("Birim yapılıyor...")
for row in range(len(matrix1)):
    index = len(matrix1) - 1 - row
    for count in range(index):
        matrix1[count] -= matrix1[index] * (
            matrix1[count][index] / matrix1[index][index]
        )


print(matrix1)

matrix1 = np.around(matrix1, decimals=6)

for index, row in enumerate(matrix1):
    print(f"x{index+1}= {row[-1]},",end="")
    if index == 5:
        print()