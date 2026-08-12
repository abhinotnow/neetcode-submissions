class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        membership = [0]*26
        #hash table :)
        for chr in s1:
            membership[ord(chr)-ord("a")] +=1
        l = 0
        r = len(s1)
        current_members = [0]*26
        for chr in s2[l:r]:
            current_members[ord(chr)-ord("a")] += 1
        if current_members == membership:
            return True
        else:
            while r<len(s2):
                current_members[ord(s2[l])-ord("a")] -=1
                current_members[ord(s2[r])-ord("a")] += 1
                l+=1
                r+=1
                if current_members == membership:
                    return True
                else:
                    continue
        return False