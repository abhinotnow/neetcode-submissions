class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [0]*length
        suffix = [0]*length
        output = [0]*length
        #prefix
        i = 0
        while i<length:
            if i == 0:
                prefix[i] = 1
                i+=1
            prefix[i] = prefix[i-1]*nums[i-1]
            i+=1
        #suffix in reverse
        i = length-1
        while i>=0:
            if i == length-1:
                suffix[i] = 1
                i+= -1
            suffix[i] = suffix[i+1]*nums[i+1]
            i-=1

        for i in range(length):
             output[i] = suffix[i]*prefix[i]
        return output

                