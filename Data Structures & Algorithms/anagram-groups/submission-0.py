class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        for word in strs:
            chrs = [0]*26
            for chr in word:
                chrs[ord(chr)-ord("a")]+=1
            key = tuple(chrs)
            if key not in words:
                words[key] = []
            words[key].append(word)
        return list(words.values())
