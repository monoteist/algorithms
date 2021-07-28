# recursion factorial
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)


# recursive len list
def recursive_len(some_list):
    if some_list == []:
        return 0
    return 1 + recursive_len(some_list[1:])


# recursive tribonacci
def tribonacci(n):
    if n in (0, 1):
        return 0
    elif n == 2:
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)


# recursive list sum
def rec_linear_sum(some_list):
    if some_list == []:
        return 0
    return some_list[0] + rec_linear_sum(some_list[1:])