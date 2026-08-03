import re 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        #stripping
        s = (re.sub(r'[^a-zA-Z0-9]',"",s)).lower()
        print(s)
        #pointers
        l = 0
        r = len(s)-1
        palindrome = True
        #even 
        if len(s)//2 == 0:
            while l<r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    palindrome = False
                    return palindrome
            return palindrome
        #odd
        else:
            while l<=r:
                if s[l] == s[r]:
                    l+=1
                    r-=1
                else:
                    palindrome = False
                    return palindrome
            return palindrome
        