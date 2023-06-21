import math


def solve_master_theorem(a, b, c, k):
    p = math.log(a) / math.log(b)
    result = ""
    if float_equals(p, c):
        result += format_poly_log(c, k + 1)
    elif p < c:
        result += format_poly_log(c, k)
    elif p > c:
        if float_equals(round(p), p):
            result += format_poly_log(round(p), 0)
        else:
            result += format_poly_log(f"log_{b}({a})", 0)
    else:
        result = "Arithmetic error"

    recurrence_text = f"T(n) = {a if a != 1 else ''}T(n{f'/{b}' if b != 1 else ''}) + Θ({format_poly_log(c, k)})"
    print(f"Recurrence text (check if it matches what you put in):"
          f"\n{recurrence_text}")
    return result


def float_equals(x, y):
    return abs(x - y) < 1e-9


def format_poly_log(c, k):
    if c == 0 and k != 0:
        result = ""
    elif c == 0 and k == 0:
        result = "1"
    elif c == 0.5:
        result = "sqrt(n)"
    elif c == 1:
        result = "n"
    else:
        c = str(c)

    if isinstance(c, str):
        result = f"n^{c}"

    if k != 0:
        result += "log"
        if k != 1:
            result += f"^{k}"
        result += " n"

    return result


if __name__ == "__main__":
    print("Format:"
          "\nT(n) = aT(n/b) + Θ(n^k (log n)^i"
          "\nOBS If the answer gives something like log^2(n) which does not match one of the cases, then it cannot be solved")

    a = float(input("Enter a:\n"))
    b = float(input("Enter b:\n"))
    c = float(input("Enter c:\n"))
    k = float(input("Enter k:\n"))
    solved = solve_master_theorem(a, b, c, k)
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