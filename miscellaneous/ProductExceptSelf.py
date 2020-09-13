class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        cum_left = [1]*len(nums)
        cum_right = [1]*len(nums)
        to_return = [None]*len(nums)
        for i in range(1,len(nums)):
            cum_left[i] = nums[i-1]*cum_left[i-1]
        for i in range(len(nums)-2,-1,-1):
            cum_right[i] = nums[i+1]*cum_right[i+1]
        for i in range(len(nums)):
            to_return[i] = cum_left[i]*cum_right[i]
        return to_return
            
        
            