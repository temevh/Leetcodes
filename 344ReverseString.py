def reverseString(s):
    toReturn = [0] * len(s)
    index = 0
    for i in reversed(s):
        toReturn[index] = i
        index += 1

    return toReturn


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
