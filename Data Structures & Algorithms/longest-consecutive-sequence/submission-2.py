class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in seen:
                long = 1
                seq = num
                while seq+1 in seen:
                    long += 1
                    seq+=1
                if long>longest:
                    longest = long
        return longest