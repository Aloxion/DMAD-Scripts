import math

def master_theorem(a, b, c):
    # compute log_b(a)
    log_b_a = math.log(a, b)

    # Case 1: If f(n) = O(n^c), where c < log_b(a)
    if c < log_b_a:
        return "T(n) = Θ(n^" + str(log_b_a) + ")"

    # Case 2: If f(n) = n^c = n^log_b(a)
    elif c == log_b_a:
        return "T(n) = Θ(n^" + str(c) + " * log(n))"

    # Case 3: If f(n) = Ω(n^c), where c > log_b(a)
    elif c > log_b_a:
        # the regularity condition cannot be checked programmatically and must be verified separately
        return "T(n) = Θ(n^" + str(c) + ") if the regularity condition is satisfied"

    else:
        return "Input Error!"

# example usage
print(master_theorem(3, 3, 0.5))  # Your specific inputs
