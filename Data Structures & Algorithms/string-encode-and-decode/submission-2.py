class Solution:
    

    def encode(self, strs: List[str]) -> str:
        output = ""
        for word in strs:
            output+= f"{len(word)}#{word}"
        return output


    def decode(self, s: str) -> List[str]:
        i = 0
        output = []
        while i < len(s):
            j = i
            while s[j] != "#":
                j+=1
            length = int(s[i:j])
            word = "".join(s[j+1:j+length+1])
            output.append(word)
            i = j+length+1
        return output


