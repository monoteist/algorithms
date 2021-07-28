# recursion factorial
def fact(x):
    if x == 1:
        return 1
    return x * fact(x - 1)



#recursive len list
def recursive_len(some_list):
    if some_list == []:
        return 0
    return 1 + recursive_len(some_list[1:])