def fib (pos):
    res = 0;
    if pos == 0:
        res = 1
    elif pos == 1:
        res = 1
    elif pos == 2:
        res = 2
    else:
        res = fib(pos-1) + fib(pos -2)
    return res


print(fib(30))
