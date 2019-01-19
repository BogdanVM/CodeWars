def disemvowel(string):
    for vowel in "aeiouAEIOU":
        string = string.replace(vowel, '')
    
    return string