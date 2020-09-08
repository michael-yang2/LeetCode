class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = 1
        to_return = 1
        for i in range(1, len(nums)):
            longest_subs = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    longest_subs = max(longest_subs, dp[j]+1)
            dp[i] = longest_subs
            to_return = max(to_return, dp[i])
        return to_return