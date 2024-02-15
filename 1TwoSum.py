def twoSum(nums, target):
    result = [0,0]
    nums.sort()
    for i in range(len(nums)):
        for j in range(len(nums)):
            if(nums[i] + nums[j] == target):
                result[0] = i
                result[1] = j
                return result

    return result


nums = [2, 7, 11, 15]
target = 9
print(twoSum(nums, target))