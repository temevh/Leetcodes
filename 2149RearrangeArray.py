
def rearrangeArray(nums):
    toReturn = []
    pos = []
    neg = []
    #1. Joka toinen pos ja neg
    #2. Samanmerkkisillä järjestys säilyy
    #3. Uusi array alkaa positiivisella
    for num in nums:
        if (num < 0):
            neg.append(num)
        else:
            pos.append(num)

    count, negCount, posCount = 0, 0, 0
    for num in nums:
        if count % 2 == 0:
            n = pos[posCount]
            toReturn.append(n)
            posCount += 1
        else:
            n = neg[negCount]
            toReturn.append(n)
            negCount += 1
        count += 1

    return toReturn


nums = [3,1,-2,-5,2,-4] 
print(rearrangeArray(nums)) # Tulisi olla [3,-2,1,-5,2,-4]
