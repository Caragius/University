

row = int(input("Количество строк: "))
column = int(input("Количество столбцов: "))
matrix = []
print("Введите значения матрицы ")
for i in range(row):
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(column):
        print(matrix[i][j], end=' ')
    print()


swap1 = int(input("Введите номер строки для обмена (нумерация начинается с нуля) "))
swap2=int(input("Введите номер строки для обмена (нумерация начинается с нуля) "))
matrix[swap1], matrix[swap2] = matrix[swap2], matrix[swap1]

for d in matrix:
    print((d))
