def binary_search(list_, item):
    low = 0
    high = len(list_) - 1

    while low <= high:
        mid = int((low + high) / 2)
        guess = list_[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

binary_search([1, 4, 7, 9], 3)
