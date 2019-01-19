def is_isogram(string):
    apps = {}
    string = string.lower()
    for char in string:
        if char in apps:
            return False
        
        apps[char] = 1
    
    return True