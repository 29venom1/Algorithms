def countdown(i):  # countdown
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)


countdown(10)


def fact(x):  # factorial
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)


print(fact(5))
