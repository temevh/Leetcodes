#PASSING, beats 99% in runtime(11ms)
def subtractProductAndSum(n):
    nums = []
    for letter in str(n):
        nums.append(int(letter))

    prod = 1
    sum = 0
    for num in nums:
        prod = prod * num
        sum = sum + num

    return prod-sum



print(subtractProductAndSum(234))