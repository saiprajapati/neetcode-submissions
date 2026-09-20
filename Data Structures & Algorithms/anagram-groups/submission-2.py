from collections import Counter

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable = {}
        lst = []
        for i in strs:
            ht = Counter(i)
            key = tuple(sorted(ht.items()))
            if key in hashtable:
                hashtable[key].append(i)
            else:
                hashtable[key] = [i]
        lst = list(hashtable.values())
        return lst