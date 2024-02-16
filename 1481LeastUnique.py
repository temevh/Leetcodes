#arraysta poistetaan k verran elementtejä, mikä on pienin mahdollinen määrä uniikkeja elementtejä
# (eli maksimimäärä duplikatejag)
#Dictionary jossa jokainen numero ja määrä -> poistetaan vaan k "harvinaisimmat"

def findLeastNumOfUniqueInts(arr, k):
    dict = {}
    for i in range(len(arr)):
        if (arr[i] in dict):
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1

    print(dict)

    amount = 0
    return amount


arr = [5,5,4]
k = 1
print(findLeastNumOfUniqueInts(arr,k))