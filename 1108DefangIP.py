def defangIPaddr(address):
    x = ""
    for letter in address:
        if letter == ".":
            x += ("[.]")
        else:
            x += letter
    return x
            

print(defangIPaddr("1.1.1.1"))