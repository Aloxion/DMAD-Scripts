import math

def master_theorem(a, b, c):
    # compute log_b(a)
    log_b_a = math.log(a, b)
    if c < log_b_a:
        return "T(n) = Θ(n^" + str(log_b_a) + ")"
    elif c == log_b_a:
        return "T(n) = Θ(n^" + str(c) + " * log(n))"
    elif c > log_b_a:
        return "T(n) = Θ(n^" + str(c) + ")"
    else:
        return "Input Error!"

# example usage
print(master_theorem(3, 3, 1))