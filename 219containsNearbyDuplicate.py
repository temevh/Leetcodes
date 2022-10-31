#Daily leetcode problem 219. Returns true if two distinct list objects are within k units of each other

#PASSING. Beats 76.63% in runtime(701ms) and 14% in memory usage(25MB)
def containsNearbyDuplicate(nums, k):
    dict = {}
    for i in range(len(nums)):
        if nums[i] in dict and abs(dict[nums[i]]-i) <= k:
            return True
        dict[nums[i]] = i

    return False

nums = [1,2,3,1]
k = 3
print(containsNearbyDuplicate(nums, k))
