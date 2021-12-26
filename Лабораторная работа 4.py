


list = [11,12,-11,-2,-3,-4,5,6,1,3]
print(list)
j=0
b = list.index(min(list, key=lambda i: int(i)))  # Ищем минимальный элемент
n = len(list)
for i in list[b:n]:
    if i < 0:


        j+=1
        if j == 4: # 4 потому что у нас есть наш минимальный элемент и от него еще 2, то есть искомый элемент будет 4
            a = list.index(i)


    else:
        pass


list[b],list[a] = list[a],list[b] # меняем их местами

print(list)

