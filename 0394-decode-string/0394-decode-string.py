class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        currentNum = 0
        currentString = ""
        # [가 시작되면 앞에 있던 수는 currentNum로 저장되고, 앞에 있던 문자는 lastString로 유지
        # ]로 끝나면 저장된 num과 str을 pop()
        # [가 안나온다면 그대로 추가
        for c in s:
            if c.isdigit():
                currentNum = currentNum*10 + int(c)
            elif c == "[":
                stack.append(currentString)
                stack.append(currentNum)
                currentString = ""
                currentNum = 0
            elif c == "]":
                num = stack.pop()
                lastString = stack.pop()
                currentString = lastString + currentString * num
            else:
                currentString += c
                
        return currentString