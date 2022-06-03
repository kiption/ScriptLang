
class Player:
    UPPER = 6
    LOWER = 7

    def __init__(self, name):
        self.name = name
        itemcount = self.UPPER+self.LOWER
        self.scores = [0 for i in range(itemcount)] # 13개 category 점수
        self.used = [False for i in range(itemcount)]    # 13개 caterory 사용여부

    def setScore(self, score, index):   # index번째 점수 set
        self.scores[index] = score

    def setAtUsed( self, index):    # index번째 사용여부 set
        self.used[index] = True

    def getTotalScore(self):
        return sum(self.scores)

    def getUpperScore(self):    # 상단 점수 합계 반환
        return sum(self.scores[:self.UPPER])

    def getLowerScore(self):    # 하단 점수 합계 반환
        return sum(self.scores[-self.LOWER:])

    def toString(self):     # 이름 반환
        return self.name

    def allUpperUsed(self):    # UPPER category 전부 사용되을 때 True, 그외는 False 반환
        for i in range(self.UPPER):
            if self.used[i] == False:
                return False
        return True

    def allLowerUsed(self):    # LOWER category 전부 사용되을 때 True, 그외는 False 반환
        i = self.UPPER
        for _i in range(self.LOWER):
            if self.used[i] == False:
                return False
            i = i + 1
        return True
