from collections import Counter
import openpyxl  # Модуль для работы с Exel

wb = openpyxl.reader.excel.load_workbook(filename="лаба 2.xlsx")

wb.active = 0
sheet = wb.active
list = []
for i in range(2, 9):
    list.append(sheet['A' + str(i)].value)

print("Изначальный список", str(list))
list.sort()

# сортировка по байту частоты элементов

result = [item for items, c in Counter(list).most_common()

          for item in [items] * c]

# печать окончательного результата

print("Отсортированный список", str(result))
