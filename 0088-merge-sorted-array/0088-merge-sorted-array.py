class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        아무것도 반환하지 않고, 정답을 nums1에 치환하는 문제
        """
        if m < 1:
            nums1[:] = nums2[:n]
        elif n < 1:
            nums1[:] = nums1[:m]
        else:
            nums1[:] = sorted(nums1[:m] + nums2[:n])
        