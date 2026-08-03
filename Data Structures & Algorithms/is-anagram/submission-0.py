class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        chrs = [0]*26
        if len(s) != len(t):
            return False
        else:
            for i in range(len(s)):
                chrs[ord(s[i])-ord("a")] += 1
                chrs[ord(t[i])-ord("a")] -= 1
            for element in chrs:
                if element != 0:
                    return False
            return True