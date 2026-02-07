import string

def wordPattern(pattern: str, s: str) -> bool:
    lSplitSentence = s.split(' ')
    dWords = {}
    dPattern = {}
    finalPattern = ''

    if (len(pattern) != len(lSplitSentence)):
        return False

    for sWord, sPattern in zip(lSplitSentence, pattern):
        
        if sWord in dWords and dWords[sWord] != sPattern:
            return False
        elif sWord not in dWords and sPattern in dPattern:
            return False
        else:
            dWords[sWord] = sPattern
            dPattern[sPattern] = sWord
        finalPattern += dWords[sWord]
        print (dWords)
    print (finalPattern)
    return (finalPattern == pattern)

#print (wordPattern("aaaa", "dog cat cat dog"))
print (wordPattern("a", "a"))