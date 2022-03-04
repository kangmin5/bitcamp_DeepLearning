import random

from hello.domains import my100, myRandom, Member, members


class Quiz00:
    def quiz00calculator(self)-> float:
        a = random.randint(1,100)
        b = random.randint(1,100)
        op=['+','-','*','/','%']

        res=op[random.randint(0,4)]
        if(res=='+'):  print(f'{a}+{b}={a+b}')
        elif(res=='-'):  print(f'{a}-{b}={a-b}')
        elif(res =='*'):  print(f'{a}*{b}={a*b}')
        elif(res=='/'):  print(f'{a}/{b}={a/b}')
        elif(res=='%'):  print(f'{a}%{b}={a%b}')

        return None

# ---------------------------------------------------
    def quiz01bmi(self):
        this = Member()
        this.name = '홍길동'
        this.height = 170.8
        this.weight = 120.8
        res = this.weight / (this.height * this.height) * 10000
        if res > 25:
            print(f'비만')
        elif res > 23:
            print(f'과체중')
        elif res > 18.5:
            print(f'정상')
        else:
            print(f'저체중')

        return None
# ----------------------------------------------------------
    def quiz02dice(self):
        print(random.randint(1, 6))
        return None
# ----------------------------------------------------------------
    def quiz03rps(self):
        p=int(input('1.가위 2.바위 3.보'))
        c=random.randint(1,3)
        if c-p == 2 or c-p == -1:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)승리')
        elif c - p == 1 or c - p == -2:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)패배')
        elif c - p == 0:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)무승부')
        else : "break"

        return None
# ----------------------------------------------------------------
    def quiz04leap(self):
        year = int(input('년도입력:'))
        if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
            print('윤년입니다')
        else:
            print('평년입니다')
        return None
# -------------------------------------------------------------
    def quiz05grade(self):
        kor = random.randint(0,100)
        eng = random.randint(0, 100)
        math = random.randint(0, 100)
        sum = kor+eng+math
        avg = (kor+eng+math) /3
        if avg >= 90:grade = 'A'
        elif avg >= 80:grade = 'B'
        elif avg >= 70:grade = 'C'
        elif avg >= 65:grade = 'D'
        elif avg >= 60:grade = 'E'
        else:
            grade = 'F'
            if grade == 'F':passChk = '불합격'
            else:passChk = '합격'
        print (f'합계{sum},평균{avg},등급{grade},합격{passChk} ')
        return None
# --------------------------------------------------------------
    def quiz06memberChoice(self):
        student = members()
        res= student[(random.randint(0, 23))]
        print(f'선택 학생은 {res}')
        return None
# -----------------------------------------------------------------
    def quiz07lotto(self):
        res = random.sample(range(1,46),6)
        print(f'로또 번호는 {res}')
        return None
# -----------------------------------------------------------------
    def quiz08bank(self, balance=0):  # 이름, 입금, 출금만 구현
        name = str(input('이름 :'))
        while 1 :
            menu = int(input('0.종료 1. 입금 2. 출금'))
            if menu == 0:
                break
            elif menu ==1:
                save = int(input('입금액:'))
                balance +=save
                print(f'잔액은 {balance}')
            elif menu ==2:
                withdrawal = int(input('출금액:'))
                balance -= withdrawal
                print((f'잔액은 {balance}'))
        return None
# -----------------------------------------------------------------
    def quiz09gugudan(self):  # 책받침구구단
        for y in range(1,10):
            for x in range(2,10):
                print(x,'x', y, '=', x*y, end='\t')
            print()
        return None