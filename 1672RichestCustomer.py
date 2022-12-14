def maximumWealth(accounts):
    biggest = 0
    biggestAcc = 0
    for elem in accounts:
        if sum(elem) >= biggest:
            biggest = sum(elem)
            #biggestAcc = accounts.index(elem)

    return biggest


print(maximumWealth([[1, 2, 3], [3, 2, 1]]))
