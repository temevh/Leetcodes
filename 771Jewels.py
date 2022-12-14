# PASSING, beats 92% in runtime(16ms)
def numJewelsInStones(jewels, stones):
    matches = 0
    for letter in stones:
        if letter in list(jewels):
            matches += 1

    return matches


print(numJewelsInStones("aA", "aAAbbbb"))
