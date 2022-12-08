# Passing, runtime 164ms, beats 87%
def reverseString(s):
    s[:] = s[::-1]


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
