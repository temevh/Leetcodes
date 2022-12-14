# PASSING, beats 95% in runtime (35ms)
def maximumWealth(accounts):
    biggest = 0
    for elem in accounts:
        if sum(elem) >= biggest:
            biggest = sum(elem)

    return biggest


print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
