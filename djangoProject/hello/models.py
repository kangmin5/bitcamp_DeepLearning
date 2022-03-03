import random
import domains


class Quiz01Calcurator():

    def __init__(self, num1, num2, opcode):
        self.num1 = num1
        self.num2 = num2
        self.opcode = opcode

    def add(self):
        return self.num1 + self.num2
    def sub(self):
        return self.num1 - self.num2
    def mul(self):
        return self.num1 * self.num2
    def div(self):
        return self.num1 / self.num2


class Quiz02Bmi(object):
    @staticmethod
    def bmi(member):
        this = member
        bmi = (this.weight / (this.height ** 2)) * 10000

        if bmi >= 30.0:
            return f'{bmi} 비만'
        elif 25.0 <= bmi < 30.0:
            return f'{bmi} 과체중'
        elif 18.5 <= bmi < 25.0:
            return f'{bmi} 정상'
        else:
            return f'{bmi} 저체중'

        return bmi

class Quiz03Grade():
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3


class Quiz04GradeAuto():
    def __init__(self, name, kor, eng, math, grade):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
        self.grade = grade

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3

    def getGrade(self):
        kor=self.kor
        eng=self.eng
        math = self.math
        if (kor | eng | math) >= 90:
            grade = "A"
        elif (kor | eng | math) >= 80:
            grade = "B"
        elif (kor | eng | math) >= 70:
            grade = "C"
        elif (kor | eng | math) >= 60:
            grade = "D"
        else:
            grade = "F"
        return grade

    def chkPass(self):  # 60점 이상이면 합격
        pass


# -----------------------------------------------------
def myRandom(start,end):
    return random.randint(start,end)

class Quiz05Dice(object):
    @staticmethod
    def getDice():
        return myRandom(1,6)

# ----------------------------------------------------
class Quiz06RandomGenerator(object):
    pass

# -----------------------------------------------------

class Quiz07RandomChoice(object):
    def __init__(self): # 803호에서 랜덤으로 1명 이름 추출
        self.members = ['홍정명', '노홍주', '전종현', '정경준', '양정오',
                        "권혜민", "서성민", "조현국", "김한슬", "김진영",
                        '심민혜' , '권솔이', '김지혜' , '하진희' , '최은아',
                        '최민서', '한성수', '김윤섭', '김승현',
                        "강 민", "최건일", "유재혁", "김아름", "장원종"]

    def chooseMember(self):
        return self.members[myRandom(1,3)]

class Quiz08Rps(object):
    def __init__(self ,player):
        self.player =player
        self.computer = myRandom(0,2)
    def game(self):
        p= self.player
        c= self.computer
        rps = ["가위","바위","보"]
        result = {0: f'컴결과{rps[c]} 플레이어가 승리했습니다.', 1: f'컴결과{rps[c]} 플레이어가 패배했습니다.', 2: f'컴결과{rps[c]}  비겼습니다.'}


        if p == c:
            state = 2
        elif p == '가위' and c == '바위':
            state = 1
        elif p == '바위' and c == '보':
            state = 1
        elif p == '보' and c == '가위':
            state = 1
        else:
            state = 0
        return result[state]



class Quiz09GetPrime(object):
    def __init__(self):
        pass
class Quiz10LeapYear(object):
    def __init__(self,year):
        self.year = year
    def leap(self):
        if(self.year %4 == 0) and (self.year %100 !=0) or (self.year %400 ==0):
            return '윤년입니다'
        else:
            return '윤년이 아닙니다'

class Quiz11NumberGolf(object):
    def __init__(self):
        pass
# ----------------------------------------------
class Quiz12Lotto(object):
    def lotto(self):
       return random.sample(range(1,46),6)

# ---------------------------------------------------------
class Quiz13Bank(object): # 이름, 입금, 출금만 구현
    def __init__(self,name,save,withdrawal,balance):
        self.name = name
        self.save = save
        self.withdrawal=withdrawal
        self.balance = balance
    def bank(self):
        self.balance =0
        self.save += self.balance
        self.withdrawal -= self.balance
        return self.balance
# ---------------------------------------------------------
class Quiz14Gugudan(object): # 책받침구구단

    def gugudan(self):
        for y in range(1,10):
            for x in range (2,10):
                print(x, 'x', y, '=', x*y, end='\t')
            print()
# ----------------------------------------------------------

