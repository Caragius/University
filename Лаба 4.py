
izn_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6]
#
print(izn_list)
min = izn_list.index(min(izn_list))
max = izn_list.index(max((izn_list)))
#min, max = max, min
izn_list[min], izn_list[max] = izn_list[max], izn_list[min]
#print(max)
print(izn_list)