# PASSED, runtime 95ms, beats 91%
def buildArray(nums):
    ans = [0] * len(nums)
    for i in nums:
        ans[i] = nums[nums[i]]
    return ans


nums = [0, 2, 1, 5, 3, 4]
print(buildArray(nums))
