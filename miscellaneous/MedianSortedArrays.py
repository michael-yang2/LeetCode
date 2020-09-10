class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        if len(nums1) == 0:
            if len(nums2) % 2== 0:
                return (nums2[len(nums2)//2-1]+nums2[len(nums2)//2])/2
            return nums2[len(nums2)//2]
        low = -1
        high = len(nums1)-1
        while low <= high:
            nums1partition = (low+high)//2
            nums2partition = (len(nums1)+len(nums2)+1)//2 - nums1partition - 2
            maxleftnums1 = nums1[nums1partition] if nums1partition >= 0 else -sys.maxsize
            minrightnums1 = nums1[nums1partition+1] if nums1partition+1 < len(nums1) else sys.maxsize
            maxleftnums2 = nums2[nums2partition] if nums2partition >= 0 else -sys.maxsize
            minrightnums2 = nums2[nums2partition+1] if nums2partition+1 < len(nums2) else sys.maxsize
            if minrightnums1 >= maxleftnums2 and minrightnums2 >= maxleftnums1:
                if (len(nums1)+len(nums2)) % 2 == 0:
                    return (max(maxleftnums1, maxleftnums2) + min(minrightnums1, minrightnums2))/2
                return max(maxleftnums1, maxleftnums2)
            elif maxleftnums1 > minrightnums2:
                high = nums1partition-1
            else:
                low = nums1partition+1
        return -1