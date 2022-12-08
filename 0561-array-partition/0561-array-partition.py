class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # 두개의 숫자를 짝짓고 그 중에서 작은수를 택하기 때문에
        # 총합이 커지기 위해선 큰수는 큰수와 짝지어지는 것이 중요하다
        nums.sort()
        pair = []
        total = 0
        for num in nums:
            pair.append(num)
            if len(pair) == 2:
                total += min(pair)
                pair = []
        return total
        