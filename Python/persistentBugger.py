def persistence(n):
    pers = 0
    while n > 9:
        temp = n
        n = 1
        while temp > 0:
            n *= temp % 10 
            temp = temp // 10
        pers = pers + 1
        
    return pers