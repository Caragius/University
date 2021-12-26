import numpy as np   # Импортирую модуль для работы с матрицами

row = int(input("Количество строк: "))
column = int(input("Количество столбцов: "))
matrix = []
print("Введите значения матрицы ")
for i in range(row):  # Создаем матрицу с заданными параметрами
    a = []
    for j in range(column):
        a.append(int(input()))
    matrix.append(a)
for i in range(row):
    for j in range(column):
        print(end=' ')
    print()

print("Изначальная матрица: ")
for d in matrix:  # Выводим изначальную матрицу
    print((d))

print(" ")

a = np.max(matrix, axis=0) # Находим максимумы по столбцам

result = np.vstack((matrix, a))  # Добавляем строку в матрицу

# print (str(result))     #  Еще один вариант вывода
print("Матрица со строкой по максимумам столбцов: ")
for d in result:    #
    print((d))
