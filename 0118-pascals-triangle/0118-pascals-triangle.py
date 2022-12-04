class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        numbers = []
        temp = []
        for i in range(numRows):
            temp.append(1)
            if i > 0:
                try:
                    for j in range(1,len(protemp)):
                        temp.append(protemp[j-1]+protemp[j])
                except:
                    pass
                temp.append(1)
            numbers.append(temp)
            protemp = temp
            temp = []
        return numbers
        