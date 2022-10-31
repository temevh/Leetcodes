#This program checks the given list(nums) for given target. If target is in list, return the index, if not, return the index where it would be inserted (in order)

#18.10.2022

#Improved version.
#PASSING. Beating 30% in runtime(73ms) and 7.69% in memory usage(14.4MB)
def searchInsert(nums, target):
    if target in nums:
        return(nums.index(target))
    else:
        if target > max(nums):
            return(len(nums))
        else:
            return(next(x[0] for x in enumerate(nums) if x[1] > target))
            

nums = [1,3,5,6]
target = 2
print(searchInsert(nums, target))


#Passing, beating 5.7% in runtime(485ms) and 7.69% in memory usage (14.4MB) :D
'''
def searchInsert(nums, target):
    for i in nums:
        if i == target:
            return(nums.index(target))
        elif i > target:
            return(nums.index(i))
        elif target > max(nums):
            return(len(nums))
    
'''