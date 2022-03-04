import random
import domains_origin


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
    def game(self):
        while 1:
            p = int(input('0.가위 1.바위 2.보 3.EXIT'))
            c = myRandom(0, 2)
            if p == 3:
                return 'EXIT'
            if c-p == 2 or c-p == -1:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:WIN')
            elif c-p == 1 or c-p == -2:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:LOSE')
            elif c-p == 0:
                print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:DRAW')




class Quiz09GetPrime(object):
    def prime(self):
        a = int(input('최대값'))
        res = ''
        for i in range(2, a):
            num = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    num += 1
            if num == 1:
                res += str(i) + '\t'
        return res



class Quiz10LeapYear(object):
    def __init__(self,year):
        self.year = year
    def leap(self):
        if(self.year %4 == 0) and (self.year %100 !=0) or (self.year %400 ==0):
            return '윤년입니다'
        else:
            return '평년입니다'

class Quiz11NumberGolf(object):
    def __init__(self):
        self.static = myRandom(0, 100)

    def game(self):
        st = self.static
        count=0
        while 1:
            se = int(input('숫자!'))
            if st == se:
                return f'정답\n 틀린횟수:{count}'
            elif st > se:
                count += 1
                print('업')
            elif st < se:
                count += 1
                print('아래')
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

