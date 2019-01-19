def array_diff(a, b):
    for x in b:
        a = list(filter(lambda n: n != x, a))
    return a