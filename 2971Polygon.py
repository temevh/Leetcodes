#Valitse numsista ne 3 numeroa joiden summa on mahdollisimman lähellä (mutta pienempi) kuin maximi
def largestPerimeter(nums):
    perimeter = 0
    if (len(nums) < 3):
        print("size return")
        return -1
    maxSide = max(nums)
    print("max side", maxSide)
    if((sum(nums) - maxSide) < maxSide):
        print("sum return")
        return -1




    return perimeter



nums = [5,5,5]
print(largestPerimeter(nums))