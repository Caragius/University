

list = [] # Список чисел
print("Введите значения списка")
print("Для выхода наберите exit или выход ")
while True: # Вечный цикл
    a = input()
    if a == "exit" or a == "выход": # Условие выхода из цикла
        break
    else:
        a = int(a)
        list.append(a)

print("Изначальный список: ")
print(list)

print("Удаляем отрицательные числа:")
list = [i for i in list if i >= 0]

print(list)


