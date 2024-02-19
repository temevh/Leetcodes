def getConcatenation(nums):
    result = [None] * 2*len(nums)

    for i in range(len(nums)):
        result[i] = nums[i]
        result[i+len(nums)] = nums[i]

    return result


nums = [1,2,1]
print(getConcatenation(nums))
