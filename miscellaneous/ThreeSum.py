class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        to_return = []
        i=0
        while i < len(nums):
            j = i+1
            k = len(nums)-1
            while j < k:
                if nums[i]+nums[j]+nums[k] == 0:
                    to_return.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                elif nums[i]+nums[j]+nums[k] < 0:
                    j+=1
                elif nums[i]+nums[j]+nums[k] > 0:
                    k-=1
                while j > i+1 and j < len(nums) and nums[j-1] == nums[j]:
                    j+=1
                while k < len(nums)-1 and k >= 0 and nums[k+1] == nums[k]:
                    k-=1
            i+=1
            while i > 0 and i < len(nums) and nums[i] == nums[i-1]:
                i+=1
        return to_return
            