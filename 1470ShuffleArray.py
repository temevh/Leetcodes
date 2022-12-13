#PASSING, beats 96.3% in runtime(40ms)
def shuffle(nums, n):
    arr = []
    for i in range(n):
        arr.append(nums[i])
        arr.append(nums[i+n])

    return arr


print(shuffle([2,5,1,3,4,7], 3))