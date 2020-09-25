class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        to_return = []
        def recur(curr_nums, possible_nums):
            if not possible_nums:
                to_return.append(curr_nums)
                return
            for i in range(len(possible_nums)):
                tmp = curr_nums.copy()
                tmp.append(possible_nums[i])
                recur(tmp, possible_nums[0:i]+possible_nums[i+1:])
        recur([], nums)
        return to_return
        
            