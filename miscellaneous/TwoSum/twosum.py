class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = {}
        for i in range(len(nums)):
            if nums[i] not in n:
                n[nums[i]] = i
        for i in range(len(nums)):
            if target - nums[i] in n and n[target-nums[i]] != i:
                return [i,n[target-nums[i]]]
        return[-1,-1]