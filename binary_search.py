def binary_search(list, item):
    low = 0
    high = len(list)-1

    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(1,101))
print(my_list)

print(binary_search(my_list, 70))
print(binary_search(my_list, -1))


