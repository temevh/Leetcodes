#PASSING, beats 63% in runtime(222ms)
def smallerNumbersThanCurrent(nums):
    arr =[0] * len(nums)
    ctr = 0
    for i in range(len(nums)):
        for j in nums:
            if j < nums[i]:
                ctr += 1
        arr[i] = ctr
        ctr = 0
    return arr

            

print(smallerNumbersThanCurrent([8,1,2,2,3]))