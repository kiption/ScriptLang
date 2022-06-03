class Configuration:

    configs = [
        "Categoty", "Ones", "Twos", "threes", "Fours", "Fives", "Sixes",
        "Upper Scores", "Upper Bonus(35)",
        "3 of a kind", "4 of a kind", "Full House(25)",
        "Small Straight(30)", "Large Straight(40)", "Yahtzee(50)", "Chance",
        "Lower Scores", "Total"
    ]

    @staticmethod
    def getConfigs():       # 정적 메소드 (객체 없이 사용 가능)
        return Configuration.configs

    # row에 따라 주사위 점수를 계산하여 반환. 
    # 예를 들어, row가 0이면 "Ones"가, 2이면 "Threes"가 채점되어야 함을 의미. 
    # row가 득점위치가 아닌 곳(즉, UpperScore, UpperBonus, LowerScore, Total 등)을 나타내는 경우 -1을 반환.
    @staticmethod
    def score(row, dices):       # 정적 메소드 (객체 없이 사용 가능)
        if (row >= 0 and row < 6):
            return Configuration.scoreUpper(dices, row + 1)
        elif (row == 8):
            return Configuration.scoreThreeOfAKind(dices)
        elif (row == 9):
            return Configuration.scoreFourOfAKind(dices)
        elif (row == 10):
            return Configuration.scoreFullHouse(dices)
        elif (row == 11):
            return Configuration.scoreSmallStraight(dices)
        elif (row == 12):
            return Configuration.scoreLargeStraight(dices)
        elif (row == 13):
            return Configuration.scoreYahtzee(dices)
        elif (row == 14):
            return Configuration.sumDie(dices)

    def scoreUpper(dice, num):  # 정적 메소드: 객체생성 없이 사용 가능
        result = 0
        for i in dice:
           if i.getRoll() == num:
               result += num
        return result
    # Upper Section 구성 (Ones, Twos, Threes, ...)에 대해 주사위 점수를 매 깁니다. 예를 들어,
    # num이 1이면 "Ones"구성의 주사위 점수를 반환합니다.


    def scoreThreeOfAKind(dice):
        dic = {}
        result = 0
        for i in dice:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():
            if val >= 3:
                return result
        return 0


    def scoreFourOfAKind(d):
        dic = {}
        result = 0
        for i in d:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():

            if val >= 4:
                return result
        return 0

    def scoreFullHouse(dice):
        dic = {}
        L=[]
        result = 0
        for i in dice:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():
            L.append(val)

        if 3 in L and 2 in L:
            return 25
        return 0
    def scoreSmallStraight(dice):
        dl = [0] * 6
        for i in range(5):
            dl[dice[i].getRoll() - 1] = 1

        result = False
        for i in range(3):
            cnt = 0
            for j in range(i, i + 4):
                if (dl[j] == 1):
                    cnt += 1
            if cnt >= 4:
                result = True
                break
        if result:
            return 30
        else:
            return 0
    # 1 2 3 4 혹은 2 3 4 5 혹은 3 4 5 6 검사
    # 1 2 2 3 4, 1 2 3 4 6, 1 3 4 5 6, 2 3 4 4 5


    def scoreLargeStraight(dice):
        result = []

        for x in dice:
            result.append(x.getRoll())
        a = set(result)
        if a =={1, 2, 3, 4, 5}:
            return 40
        elif a == {2, 3, 4, 5, 6}:
            return 40
        else:
            return 0
    # 1 2 3 4 5 혹은 2 3 4 5 6 검사


    def scoreYahtzee(dice):
        dic = {}
        result = 0
        for i in dice:
            result += i.getRoll()
            try:
                dic[i.getRoll()] += 1
            except:
                dic[i.getRoll()] = 1

        for key, val in dic.items():

            if val == 5:
                return 50
        return 0

    def sumDie(dice):
        result = 0
        for i in dice:
            result += i.getRoll()
        return result

