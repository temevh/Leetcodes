#PASSING, beats 88% in runtime(27ms)
def runningSum(nums):
    sum = 0
    arr = []
    for num in nums:
        total = sum + num
        arr.append(total)
        sum += num
    return arr

nums = [1,2,3,4]
print(runningSum(nums))