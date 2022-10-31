#A program that returns the sum of two given binary strings as a binary string


#PASSING. Beats 99.42% in runtime(12ms) and 50% in memory usage(13.6MB)
def addBinary(a,b):
    return(bin(int(a,2)+int(b,2))) [2:]


a = "11"
b = "1"
print(addBinary(a,b))


#PASSING. Beating 31.6% in runtime(47ms) and 75% in memory usage(13.4MB)
'''
def addBinary(a,b):

    a,b =int(a,2), int(b,2)
    return(bin(a+b).replace("0b", ""))
'''
