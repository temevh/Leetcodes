
# PASSING, runtime 69ms, beats(85%)
def getConcatenation(nums):
    toReturn = [0] * (2 * len(nums))

    index = 0
    for i in nums:
        toReturn[index] = i
        toReturn[index+len(nums)] = i
        index += 1
    return toReturn


nums = [1, 2, 1]
print(getConcatenation(nums))


# PASSING, runtime 155ms (beats 31%)
def getConcatenation2(nums):
    toReturn = []
    for i in nums:
        toReturn.append(i)
    for i in nums:
        toReturn.append(i)
    return toReturn
