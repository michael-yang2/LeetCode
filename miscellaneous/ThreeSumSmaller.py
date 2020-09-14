class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if len(nums) < 3:
            return 0
        nums.sort()
        to_return = 0
        i=0
        while i < len(nums):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] < target:
                    to_return+=(k-j)
                    j+=1
                else:
                    k-=1
            i+=1
        return to_return