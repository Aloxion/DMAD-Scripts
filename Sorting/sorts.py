import heapq

def counting_sort(arr):
    max_val = max(arr)
    m = max_val+1
    count = [0]*m                
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
        print(f"After counting value {a}: {arr}")
    return arr

def radix_sort(arr):
    RADIX = 10
    placement = 1
    max_digit = max(arr)

    while placement < max_digit:
        buckets = [list() for _ in range(RADIX)]
        for i in arr:
            tmp = int((i / placement) % RADIX)
            buckets[tmp].append(i)
        a = 0
        for b in range(RADIX):
            buck = buckets[b]
            for i in buck:
                arr[a] = i
                a += 1
        print(f"After sorting digits at place {placement}: {arr}")
        placement *= RADIX
    return arr

def bubble_sort(arr):
    def swap(i, j):
        arr[i], arr[j] = arr[j], arr[i]

    n = len(arr)
    swapped = True
    x = -1
    while swapped:
        swapped = False
        x = x + 1
        for i in range(1, n-x):
            if arr[i - 1] > arr[i]:
                swap(i - 1, i)
                swapped = True
        print(f"After pass {x+1}: {arr}")
    return arr

def insertion_sort(arr):
    for i in range(len(arr)):
        cursor = arr[i]
        pos = i
        while pos > 0 and arr[pos - 1] > cursor:
            arr[pos] = arr[pos - 1]
            pos = pos - 1
        arr[pos] = cursor
        print(f"After inserting element {i}: {arr}")
    return arr

def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minimum]:
                minimum = j
        arr[minimum], arr[i] = arr[i], arr[minimum]
        print(f"After pass {i+1}: {arr}")
    return arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
    return merge(left, right, arr.copy())

def merge(left, right, merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor+right_cursor]=left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]
    print(f"Merge result: {merged}")
    return merged

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    print(f"Partitioning on pivot {pivot}: {left + middle + right}")
    return quick_sort(left) + middle + quick_sort(right)

def min_heap_sort(arr):
    heapq.heapify(arr)
    sorted_arr = [heapq.heappop(arr) for _ in range(len(arr))]
    print(f"Min heap sorted array: {sorted_arr}")
    return sorted_arr

def max_heap_sort(arr):
    arr = [-1 * i for i in arr]
    heapq.heapify(arr)
    sorted_arr = [-1 * heapq.heappop(arr) for _ in range(len(arr))]
    print(f"Max heap sorted array: {sorted_arr}")
    return sorted_arr

sort_algorithms = {
    'counting': counting_sort,
    'radix': radix_sort,
    'bubble': bubble_sort,
    'insertion': insertion_sort,
    'selection': selection_sort,
    'merge': merge_sort,
    'quick': quick_sort,
    'min_heap': min_heap_sort,
    'max_heap': max_heap_sort
}

def sort_array(arr, sort_type):
    sort_func = sort_algorithms.get(sort_type)
    if not sort_func:
        raise ValueError(f'Invalid sort type: {sort_type}')
    
    sorted_arr = sort_func(arr[:])
    return sorted_arr


# example usage:
arr = [2452, 5363, 4433, 1413, 2433, 3222, 2121]
sort_type = 'selection'
print(sort_array(arr, sort_type))
