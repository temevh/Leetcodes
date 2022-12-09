
#PASSING, beats 97%, runtime 31ms
def finalValueAfterOperations(operations):
    x = 0
    for oper in operations:
        if oper == "--X" or oper == "X--":
            x -= 1
        else:
            x += 1

    return x

print(finalValueAfterOperations(["--X","X++","X++"]))


#PASSING, beats 50%, runtime(72ms)
def finalValueAfterOperations2(operations):
    x = 0
    for oper in operations:
        if oper == "--X" or oper == "X--":
            x -= 1
        elif oper == "++X" or oper == "X++":
            x += 1

    return x