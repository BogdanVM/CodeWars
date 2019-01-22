def find_it(seq):
    apps = {}
    for num in seq:
        if num in apps:
            apps[num] += 1
        else:
            apps[num] = 1
    
    return [num for num in seq if apps[num] % 2 == 1][0]