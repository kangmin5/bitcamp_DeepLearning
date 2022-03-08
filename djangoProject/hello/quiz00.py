import random

from hello.domains import my100, myRandom, Member, members


class Quiz00:
    def quiz00calculator(self) -> float:
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        op = ['+', '-', '*', '/', '%']
        res = op[random.randint(0, 4)]  # 인덱싱 (5가지중의 1개를 무작위로 뽑아낸다)
        if (res == '+'):
            print(f'{a}+{b}={a + b}')
        elif (res == '-'):
            print(f'{a}-{b}={a - b}')
        elif (res == '*'):
            print(f'{a}*{b}={a * b}')
        elif (res == '/'):
            print(f'{a}/{b}={a / b}')
        elif (res == '%'):
            print(f'{a}%{b}={a % b}')

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
        p = int(input('1.가위 2.바위 3.보'))
        c = random.randint(1, 3)
        if c - p == 2 or c - p == -1:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)승리')
        elif c - p == 1 or c - p == -2:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)패배')
        elif c - p == 0:
            print(f'플레이어: {p}\n 컴퓨터:{c}\n 결과:(플레이어)무승부')
        else:
            "break"

        return None

    # ----------------------------------------------------------------
    def quiz04leap(self):  # 윤년
        '''
            Java스타일
            s = (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0) ? "윤년" :"평년"
        '''
        y = random.randint(2000, 2022)
        s = "윤년" if (y % 4 == 0) and (y % 100 != 0) or (y % 400 == 0) else "평년"
        print(f'{y}년은 {s}입니다.')
        return None

    # -------------------------------------------------------------
    def quiz05grade(self):
        kor = random.randint(0, 100)
        eng = random.randint(0, 100)
        math = random.randint(0, 100)
        sum = kor + eng + math
        avg = (kor + eng + math) / 3
        if avg >= 90:
            grade = 'A'
        elif avg >= 80:
            grade = 'B'
        elif avg >= 70:
            grade = 'C'
        elif avg >= 65:
            grade = 'D'
        elif avg >= 60:
            grade = 'E'
        else:
            grade = 'F'
            if grade == 'F':
                passChk = '불합격'
            else:
                passChk = '합격'
        print(f'합계{sum},평균{avg},등급{grade},합격{passChk} ')
        return None

    # --------------------------------------------------------------
    def quiz06memberChoice(self):
        return members()[(random.randint(0, 23))]

    # -----------------------------------------------------------------
    def quiz07lotto(self):
        res = random.sample(range(1, 46), 6)
        print(f'로또 번호는 {res}')
        return None

    # -----------------------------------------------------------------
    def quiz08bank(self):  # 이름, 입금, 출금만 구현
        Account.main()

    # -----------------------------------------------------------------
    def quiz09gugudan(self):  # 책받침구구단
        for y in range(1, 10):
            for x in range(2, 10):
                print(x, 'x', y, '=', x * y, end='\t')
            print()
        return None


'''
08번 문제 해결을 위한 클래스는 다음과 같다.
[요구사항(RFP)]
은행이름은 Bitbank
입금자 이름(name), 계좌번호(account_number), 금액(money) 속성값으로 계좌를 생성한다.
계좌번호는 3자리-2자리-6자리 형태로 랜텀하게 생성된다. 예제 : 123-12-123456
금액은 100만원 ~ 999만원 사이로 랜덤하게 입금된다.
'''


class Account(object):
    def __init__(self,name,account_number,money):
        self.BANK_NAME = '비트은행'
        self.name = Quiz00().quiz06memberChoice() if name == None else name
        self.account_number = self.creat_account_number() if account_number == None else account_number
        self.money = random.randint(100, 999) if money ==None else money

    def to_string(self):
        return f'은행 : {self.BANK_NAME},' \
               f'입금자 : {self.name}' \
               f'계좌번호 :{self.account_number} ' \
               f'금액 : {self.money}만원'

    def creat_account_number(self):
        return "".join(["-" if i==3 or i==6  else str(random.randint(0, 9)) for i in range(13)])

    @staticmethod
    def find_account(ls,account_number):   # 검색
        # return "".join([j.to_string() if j.account_number == account_number else 'Wrong account'
        #         for i,j in enumerate(ls)])
        for i,j in enumerate(ls):
            if j.account_number == account_number:
                 a= ls[j]
        return a

    @staticmethod
    def del_account(ls,account_number):           #계좌삭제
        for i,j in enumerate(ls):                 # 처음 i 는 index  j는 value
            if j.account_number ==account_number:
                del ls[i]

    @staticmethod
    def save_account(ls,account_number):      # 입금
        deposit = int(input('입금액'))
        for i, j in enumerate(ls):  # i는 index j는 값
            if j.account_number == account_number:
                j.money = j.money + deposit
        return j.money

    @staticmethod
    def withdrawal_account(ls,account_number):      # 출금 (잔액보다 크면 불가함)
        money = int(input('출금액'))
        for i, j in enumerate(ls):  # i는 index j는 값
            if j.account_number == account_number:
                if j.money>=money :
                    j.money -= money
                else:
                    print(f'출금금액이 잔액보다 큽니다.')
                # j.money = j.money- money if j.money>=money else print(f"출금액이 큼")

        return j.money

    @staticmethod
    def main():
        ls =[]
        while 1:
            menu = input('0.종료 1.개좌개설 2.계좌내용 3.입금 4. 출금 5.계좌해지 6.계좌조회')
            if menu == '0':
                break
            if menu == '1':
                acc = Account(None,None,None)
                print(f'{acc.to_string()}...개설되었습니다.')
                ls.append(acc)
            elif menu == '2': # 계좌 내용
                a = '\n'.join(i.to_string() for i in ls )
                print(a)
            elif menu == '3':
                Account.save_account(ls, input('입금할 계좌번호'))

            elif menu == '4':
                Account.withdrawal_account(ls,input('출금할 계좌번호'))

                #추가코드완성
            elif menu == '5':
                Account.del_account(ls,input('탈퇴할 계좌번호'))

            elif menu =='6': # 계좌 조회
                print(Account.find_account(ls,input('조회할 계좌번호:') ))
            else:
                print('Wrong Number... Try Again')
                continue