#Removes a list element if it matches the given value.
#A very simple approach. Beats 46% in runtime(36ms) and 63% in memory usage(13.4mb)

def removeElement(nums, val):
    while val in nums:
        nums.remove(val)
    return(len(nums))
  

nums = [0,1,2,2,3,0,4,2]
val = 2
print(removeElement(nums, val))