#Program to transfer Roman numerals to corresponding integers, using a dictionary.
#Complexity NOT-OPTIMAL due to replace

def romanToInt(s):
    translations = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }

    sum = 0
    s = s.replace("IV", "IIII").replace("IX","VIIII")
    s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
    s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
    for char in s:
        sum = sum + translations[char]
    
    return sum

s = "MCMXCIV"
print(romanToInt(s))