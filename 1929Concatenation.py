def getConcatenation(nums):
    toReturn = []
    for i in nums:
        toReturn.append(i)
    for i in nums:
        toReturn.append(i)
    return toReturn


nums = [1, 2, 1]
print(getConcatenation(nums))
