def counting_sort(A, B, k):
    # initialize count array
    C = [0] * (k + 1)

    # count occurrences
    for i in range(len(A)):
        C[A[i]] += 1

    # find cumulative count
    for i in range(1, k+1):
        C[i] += C[i - 1]

    # place the elements in sorted order
    for i in range(len(A)-1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] -= 1

    return C


# input array
A = [2, 0, 1, 2, 3, 3, 5, 2]
B = [0] * len(A)

C = counting_sort(A, B, 5)

# calculate sum of counters
sum_of_counters = sum(C)

print(f'Sum of counters is: {sum_of_counters}')
print(f'Sorted array is: {B}')
print(f'Array C is: {C}')
