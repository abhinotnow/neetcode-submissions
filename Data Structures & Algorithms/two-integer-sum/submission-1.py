class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target-nums[i] in seen:
                j = seen[target-nums[i]]
                return [min(i,j),max(i,j)]
            else:
                seen[nums[i]] = i