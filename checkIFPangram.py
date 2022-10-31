#A program to check if a given string contains all of the letters from the English alphabet
#Daily leetcode problem for 17.10.2022
#Passing, beats 73% in runtime(25ms) and 57% in memory (13.4mb)
def checkIfPangram(sentence):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    amount = 0
    for letter in alphabet:
        if letter in sentence:
            amount += 1
        else:
            return False
    if amount == len(alphabet):
        return True


sentence = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(sentence))