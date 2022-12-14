# PASSING, beats 94% in runtime(16ms)
def numJewelsInStones(jewels, stones):
    jewArr = []
    matches = 0
    for letter in jewels:
        jewArr.append(letter)
    for letter in stones:
        if letter in jewArr:
            matches += 1

    return matches


print(numJewelsInStones("aA", "aAAbbbb"))
