# PASSING, beats 99.87% in runtime(15ms)
def mostWordsFound(sentences):
    m = 0
    for s in sentences:
        m = max(m, len(s.split()))
    return m


sentences = ["alice and bob love leetcode",
             "i think so too", "this is great thanks very much"]

print(mostWordsFound(sentences))
