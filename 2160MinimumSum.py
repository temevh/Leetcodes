def minimumSum(num):
    arr = [int(x) for x in str(num)]
    arr.sort()
    return arr[0] * 10 + arr[1] * 10 + arr[2] + arr[3]


print(minimumSum(2932))
