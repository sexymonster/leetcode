class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # 정규 표현식 사용 (단어가 아닌것들을 여백으로 치환)
        words = re.sub('[^\w]',' ',paragraph).lower().split()
        # 필터 사용 (banned에 포함되지 않은 요소만 필터링)
        words = filter(lambda x: x not in banned, words)
        # collections 모듈 사용 (가장 빈번한 단어 추출)
        counter = collections.Counter(words)
        return counter.most_common(1)[0][0]