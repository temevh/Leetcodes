#PASSING, beats 69% in runtime(23ms)
def smallestEvenMultiple(n):
    if n % 2 == 0:
        return n
    else:
        return n*2

print(smallestEvenMultiple(6))