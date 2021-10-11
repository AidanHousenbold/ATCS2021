words = ["adsdf", "sfd"]
def findWords(words):
    posWords = []
    for word in words:
        if isRow(word):
            posWords.append(word)
    return posWords

def isRow(wordIn):
    rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
    pos = True
    for row in rows:
        for letter in wordIn:
            if letter in row:
                pos = False
                break
        if pos == True:
            return True
print(findWords(words))