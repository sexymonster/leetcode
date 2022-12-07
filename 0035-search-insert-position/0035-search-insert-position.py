class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target not in nums:
            a = 0
            if nums[-1] < target:
                a = len(nums)
            else:    
                for idx, num in enumerate(nums):
                    a= 0
                    if num > target:
                        a = idx
                        break
            return a
        