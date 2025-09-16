array = [2, 4, 5, 1, 8, 6, 9, 3]

for i in range(len(array) - 1):
    min_index = i
    for j in range(i + 1, len(array)):
        if array[j] < array[min_index]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i]
    
print(array)