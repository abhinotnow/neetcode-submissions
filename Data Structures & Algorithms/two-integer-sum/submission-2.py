class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            if target-nums[i] in seen:
                num = target - nums[i]
                return [min(i,seen[num]),max(i,seen[num])]
            else:
                seen[nums[i]] = i