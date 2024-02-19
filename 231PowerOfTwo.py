#Return true if a given number n is a power of two
import math

def isPowerOfTwo(n):
    return (n !=0) and (n & (n-1) == 0)


n = 3
print(isPowerOfTwo(n))