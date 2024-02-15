#Valitse numsista ne 3 numeroa joiden summa on mahdollisimman lähellä (mutta pienempi) kuin maximi
def largestPerimeter(nums):
    perimeter = -1
    numSum = sum(nums)
    nums.sort(reverse=True)
    for i in range(len(nums)):
        numSum -= nums[i]
        if (numSum > nums[i]):
            perimeter = numSum + nums[i]
            return perimeter

    return perimeter



nums = [1,12,1,2,5,50,3]
print(largestPerimeter(nums))