def linear_hashing_find_aux(A, x):
    possible = []
    m = len(A)
    for i in range(m):
        for j in range(m):
            position = (i + j) % m
            if A[position] == None and position == x:
                possible.append(i)
            if (A[position] == None and position != x):
                break

    return possible


if __name__ == '__main__':
    #A is Array, and x is index.
    possible = linear_hashing_find_aux([33, None, 27, 32, 55, None, 47], 1)
    print(possible)