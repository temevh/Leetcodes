def topKFrequent(words, k):
    dict = {}
    for word in words:
        if word not in dict.keys():
            dict[word] = 0
        dict[word] += 1
    #print(dict)
    returnlist = []

    for key, value in dict.items():
        #print(key, value)
        if value <= k:
            returnlist.append(key)
    return returnlist


words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
k =  4
print(topKFrequent(words, k))