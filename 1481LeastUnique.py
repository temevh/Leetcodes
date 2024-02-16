#arraysta poistetaan k verran elementtejä, mikä on pienin mahdollinen määrä uniikkeja elementtejä
# (eli maksimimäärä duplikatejag)
#Dictionary jossa jokainen numero ja määrä -> poistetaan vaan k "harvinaisimmat"

def findLeastNumOfUniqueInts(arr, k):
    nums = {}
    for i in range(len(arr)):
        if (arr[i] in nums):
            nums[arr[i]] += 1
        else:
            nums[arr[i]] = 1

    sortedDict = dict(sorted(nums.items(), key=lambda item: item[1]))
    least = []
    for i in range(k): 
        least.append(next(iter(sortedDict)))
        del sortedDict[next(iter(sortedDict))] 
        
    return len(least)

arr = [4,3,1,1,3,3,2]
k = 3
print(findLeastNumOfUniqueInts(arr,k))