class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg = -sys.maxsize
        curr_avg = 0
        curr_len = 0
        for i in range(len(nums)):
            if curr_len < k:
                curr_avg = (curr_avg*curr_len+nums[i])/(curr_len+1)
                curr_len+=1
            else:
                curr_avg = curr_avg - nums[i-k]/curr_len + nums[i]/curr_len
            if curr_len == k:
                max_avg = max(max_avg, curr_avg)
        return max_avg
        