#A program that counts the times a given string can be split in a way where the parts are "balanced" (same amount of matching letters)

#PASSING. 34ms runtime (beats 43%) and 13.7MB memory usage (beats 9%)

def balancedStringSplit(s):
    r, l = 0, 0
    counter = 0
    for elem in s:
        if elem == "L":
            l += 1
        elif elem =="R":
            r += 1
        if r==l:
            counter += 1
            r, l = 0,0
    return counter
        
s= "RLRRLLRLRL"
print(balancedStringSplit(s))


#PASSING. 42ms runtime (beats 13.95%) and 13.3MB memory usage (beats 97%)
'''
def balancedStringSplit(s):
    r, counter = 0, 0
    for elem in s:
        if elem == "R":
            r += 1
        else:
            r += -1
        if r == 0:
            counter += 1
    return counter
'''

#PASSING. 42ms runtime (beats 13.95%) and 13.5MB memory usage (beats 30%)
'''
def balancedStringSplit(s):
    ret = 0
    counter = 0
    for letter in s:
        if letter == "L":
            ret = ret + 1
        else:
            ret = ret - 1
        if ret == 0:
            counter = counter + 1
    return counter
'''



