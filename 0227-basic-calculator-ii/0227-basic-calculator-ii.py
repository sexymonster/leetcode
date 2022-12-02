class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        # 부호, 숫자, 스텍 초기설정
        sign, num, stack = "+", 0, []
        # s의 인덱스와 원소 추출
        for i , c in enumerate(s):
            # 원소가 숫자일 경우 int형변환
            if c.isdigit():
                num = num*10 + int(c)
            # 원소가 부호인 경우
            # stack에 일단 처음나온 수를 넣고 부호를 뒤에 지정함으로써 후처리함(다음 부호가 나올때 계산)
            if (not c.isdigit() and not c.isspace()) or i == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    prev = stack.pop()
                    stack.append(prev*num)
                elif sign == "/":
                    prev = stack.pop()
                    if prev // num < 0 and prev % num !=0:
                        stack.append(prev//num + 1)
                    else:
                        stack.append(prev//num)
                sign = c
                num = 0
        return sum(stack)