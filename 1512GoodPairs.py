#Passing, beats 87% in runtime(21ms)
def numIdenticalPairs(nums):
    res = 0 
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                res+=1
    return res

print(numIdenticalPairs([1,2,3,1,1,3]))