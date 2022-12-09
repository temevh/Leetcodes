#PASSING, beats 90% in runtime(16ms)
def defangIPaddr(address):
    return address.replace('.','[.]')
            

print(defangIPaddr("1.1.1.1"))


#PASSING, beats 75% in runtime(22ms)
def defangIPaddr2(address):
    x = ""
    for letter in address:
        if letter == ".":
            x += ("[.]")
        else:
            x += letter
    return x
            