def bin_ser_rec(list, item):
    """binary search recursion  O(log n)"""
    low = 0
    high = len(list)-1

    mid = (low+high) // 2
    guess = list[mid]
    if guess == item:
        return mid
    elif guess < item:
        return mid + bin_ser_rec(list[mid:], item)
    else:
        return bin_ser_rec(list[:mid+1], item)


my_list = list(range(1, 11))
print(bin_ser_rec(my_list, 3))
