#A program to give the two indexes which add up to the given target

#Using a dictionary and a for loop, a better complexity can be achieved
def twosum(nums, target):
    map = dict()
    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in map:
            return [map[num], i]
        else:
            map[complement] = i


#Using a double for-loop, the complexity is O(n^2), which is too much
def twosumDoubleFor(nums, target):
    alist = []
    for i in range(0, len(nums)):
        initial = nums[i]
    for j in range(1, len(nums)):
        if nums[j] + initial == target:
            alist.append(nums.index(initial))
            alist.append(nums.index(nums[j]))
            return alist
            #return nums.index(initial), nums.index(nums[j])
        else:
            j = j + 1


nums = [3,2,4]
target = 6
print(twosum(nums, target))



