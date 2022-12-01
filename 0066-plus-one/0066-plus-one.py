class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number = 1
        for i in range(len(digits)):
            number += digits[-1-i]*(10**i)
        return [int(x) for x in list(str(number))]