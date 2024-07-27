list_1 = [1, 2, 1, 4, 6]

print(list(set(list_1)))

#remove duplicate element list in 2 set 
list_2 = [1, 2, 1, 4, 6]
list_3 = [7, 8, 2, 1]

print(list(set(list_1) ^ set(list_2)))
