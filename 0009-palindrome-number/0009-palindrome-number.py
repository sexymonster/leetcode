class Solution:
    def isPalindrome(self, x: int) -> bool:
        strx = str(x)
        ans = bool
        if strx[0] == "-":
            ans = False
        elif strx[0] != "-" and len(strx) % 2 == 1:
            for i in range(len(strx)//2):
                print(strx[i], strx[-1-i])
                if strx[i] == strx[-i-1]:
                    pass
                elif strx[i] != strx[-i-1]:
                    ans= False
                    break
        elif strx[0] != "-" and len(strx) % 2 == 0:
            for j in range(len(strx)//2):
                print(strx[j], strx[-1-j])
                if strx[j] == strx[-j-1]:
                    ans = True
                elif strx[j] != strx[-j-1]:
                    ans= False
                    break
        return ans