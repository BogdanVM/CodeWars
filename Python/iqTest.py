def iq_test(numbers):
    splitNumbers = numbers.split()
    oddNumbers = [i for i in range(0, len(splitNumbers)) if int(splitNumbers[i]) % 2 == 1]
    if len(oddNumbers) > 1:
        return [i for i in range(0, len(splitNumbers)) if int(splitNumbers[i]) % 2 == 0][0] + 1
    else:
        return oddNumbers[0] + 1