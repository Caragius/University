
list = []
while True:
    a = (input("введите элемент списка: "))
    if a != "exit":
        list.append(a)
    else:
        break
print(list)
print("Меняем первый и последний элемент")
list[0],list[-1] = list[-1], list[0]
print((list))