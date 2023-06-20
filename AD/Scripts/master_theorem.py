import math


def solve_master_theorem(a, b, k, i):
    p = math.log(a) / math.log(b)
    result = ""
    if float_equals(p, k):
        result += format_poly_log(k, i + 1)
    elif p < k:
        result += format_poly_log(k, i)
    elif p > k:
        if float_equals(round(p), p):
            result += format_poly_log(round(p), 0)
        else:
            result += format_poly_log(f"log_{b}({a})", 0)
    else:
        result = "Arithmetic error"

    recurrence_text = f"T(n) = {a if a != 1 else ''}T(n{f'/{b}' if b != 1 else ''}) + Θ({format_poly_log(k, i)})"
    print(f"Recurrence text (check if it matches what you put in):"
          f"\n{recurrence_text}")
    return result


def float_equals(x, y):
    return abs(x - y) < 1e-9


def format_poly_log(k, i):
    if k == 0 and i != 0:
        result = ""
    elif k == 0 and i == 0:
        result = "1"
    elif k == 0.5:
        result = "sqrt(n)"
    elif k == 1:
        result = "n"
    else:
        k = str(k)

    if isinstance(k, str):
        result = f"n^{k}"

    if i != 0:
        result += "log"
        if i != 1:
            result += f"^{i}"
        result += " n"

    return result


if __name__ == "__main__":
    print("Format:"
          "\nT(n) = aT(n/b) + Θ(n^k (log n)^i"
          "\nOBS If the answer gives something like log^2(n) which does not match one of the cases, then it cannot be solved")

    a = float(input("Enter a:\n"))
    b = float(input("Enter b:\n"))
    k = float(input("Enter k:\n"))
    i = float(input("Enter i:\n"))
    solved = solve_master_theorem(a, b, k, i)
    print(f"Solution:"
          f"\nΘ({solved})")

'''
Consider the following recurrence relation as an example:

T(n) = 2T(n/3) + n^4 log^5(n)

This is a more complex recurrence relation that includes a logarithmic factor. Here, we have:

a = 2 (because we divide n by 2 in the recursive part),
b = 3 (because we have 3 recursive calls),
k = 4 (because of the n term), and
i = 5 (because log(n) is squared, i.e., log^5(n)).

This example shows a case where i ≠ 0. 
Please note that such cases do not always have straightforward solutions using the Master theorem, 
and additional mathematical insight might be needed.

'''