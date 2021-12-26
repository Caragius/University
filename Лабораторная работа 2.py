import openpyxl  # Модуль для работы с Exel
wb = openpyxl.reader.excel.load_workbook(filename = "лаба 2.xlsx") # Открываем файл
#print(wb.sheetnames)  # Можно посмотреть количество листов в файле
wb.active = 0  # Указываем с каким листом работаем (счет начинается с нуля, те Лист 1 в файле здесь имеет индекс 0)
sheet = wb.active # Присваиваем значение переменной, чтобы можно было к ней обращаться
list_debtors = [] # Список для должников
list = [] # Список для умничек
for i in range(2,7): # Находим должников по условию:
            # Если ХОТЯ БЫ по 1 предмету оценка является неудовлетворительной, то человек является должником
    if int(sheet['I'+str(i)].value) < 3 or int(sheet['J'+str(i)].value) < 3 \
            or int(sheet['K'+str(i)].value) < 3 or int(sheet['L'+str(i)].value) < 3\
            or int(sheet['M'+str(i)].value) < 3:
        #print(sheet['A'+str(i)].value)  # Можно вывести фамилии отдельно
        list_debtors.append(sheet['A'+str(i)].value)

for i in range(2,7): # Создаем список из умничек
    if int(sheet['I'+str(i)].value) >= 3 and int(sheet['J'+str(i)].value) >= 3\
            and int(sheet['K'+str(i)].value) >= 3 and int(sheet['L'+str(i)].value) >= 3\
            and int(sheet['M'+str(i)].value) >= 3:
        #print(sheet['A'+str(i)].value)  # Можно вывести фамилии отдельно
        list.append(sheet['A'+str(i)].value)


list_debtors.sort() # Сортируем должников по афлавиту
list_dolg2 = [] # Изменяем список должников
for i in list_debtors: # Присваем всем должникам клеймо
    a = i + " (должник)"
    list_dolg2.append(a) # Добавлем это заклейменных в новый список

list += list_dolg2 # Соединяем списки обычных и должников

print("")
print(list) # Выводим список ВСЕХ студентов