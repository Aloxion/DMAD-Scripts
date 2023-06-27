def countingSort(array):
    size = len(array)
    output = [0] * size
    counted_array = []
    lastSum = 0
    count = [0] * 10

    for i in range(0, size):
        count[array[i]] += 1

    # Kumulative counted array
    for i in range(0, size-1):
        if (i == 0):
            counted_array.append(0)
            lastSum += count[i]
        else:
            counted_array.append(lastSum)
            lastSum += count[i]
    
    print("Array C:",counted_array)
    for i in range(1, 10):
        count[i] += count[i - 1]

    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    for i in range(0, size):
        array[i] = output[i]


data = [3, 1, 4, 3, 5, 0, 3, 1]
countingSort(data)
print("Sorted Array in Ascending Order: ")
print(data)