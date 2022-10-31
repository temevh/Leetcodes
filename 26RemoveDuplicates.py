from os import remove


#A program that removes duplicates from a list of given numbers, while maintaining the size of the list as original

def remCountuplicates(nums):
    met = []
    remCount = 0
    for i in nums:
        number = nums[i]
        if number in met:
            nums[i] = 0
            remCount += 1
        elif number not in met:
            met.append(number)
    print(nums)
    return remCount
    

nums = [0,0,1,1,1,2,2,3,3,4]
print(remCountuplicates(nums))