from collections import Counter
from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    if (len(strs) == 1):
        return [strs]
    
    wordsVisited = {}
    for word in strs:
        cword = tuple(sorted(Counter(word).items()))
        print (cword)
        if (cword not in wordsVisited.keys()):
            wordsVisited[cword] = [word]
        else:
            wordsVisited[cword].append(word)

    print (list(wordsVisited.values()))

#groupAnagrams(["eat","tea","tan","ate","nat","bat"])
groupAnagrams(["ddddddddddg","dgggggggggg"])