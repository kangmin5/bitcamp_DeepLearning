from hello.domains import Member
from hello.models import Quiz01Calcurator, Quiz03Grade, Quiz04GradeAuto, Quiz07RandomChoice, Quiz08Rps, Quiz09GetPrime, \
    Quiz10LeapYear, Quiz11NumberGolf, Quiz12Lotto, Quiz13Bank, Quiz14Gugudan, Quiz05Dice, Quiz02Bmi

if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+-*/) 2.Bmi 3.Grade 4.성적(등급까지) 5.주사위 6. 원하는범위에서1개숫자 7.멤버1명뽑기 '
                     '8.RPS 10.윤년구하기 12.Lotto 13.Bank입출금 14.책받침구구단')
        if menu == 0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            opcode: str = input('연산자')
            num2 = int(input('두번째 수'))

            q1 = Quiz01Calcurator(num1, num2, opcode)
            if opcode == '+':
                result = q1.add()
            elif opcode == '-':
                result = q1.sub()
            elif opcode == '*':
                result = q1.mul()
            elif opcode == '/':
                result = q1.div()
            print(f'{q1.num1}{opcode}{q1.num2}={result}')

        elif menu == '2':
            member =Member()
            q2=Quiz02Bmi()
            member.name =input('이름 입력')
            member.height = float(input('키 입력'))
            member.weight = float(input('몸무게 입력'))
            res = q2.bmi(member)
            print(f'이름:{member.name}, 키:{member.height}, 몸무게:{member.weight}  , BMI상태{res}')

        elif menu == '3':
            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            q3 = Quiz03Grade(name, kor, eng, math)

            print(f'{name}님의 국어{kor}{q3.g} 영어{eng} 수학{math} 이고 합계는{q3.sum()} 이고 평균은{q3.avg()} 입니다.')

        elif menu == '4':
            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            grade = ''
            q4 = Quiz04GradeAuto(name, kor, eng, math,grade)

            print(f'{name}님의 국어{kor}{q4.grade} 영어{eng} 수학{math} 이고 합계는{q4.sum()} 이고 평균은{q4.avg()} 입니다.')


        elif menu == '5':
            q5 = Quiz05Dice()
            print(f"주사위의 값은 : {q5.getDice()}")

        elif menu == '6':
            pass
# --------------------------------------------------------------
        elif menu =='7':
            q7 = Quiz07RandomChoice( )
            print(f"{q7.chooseMember()}")
# --------------------------------------------------------------
        elif menu =='8':
            player = int(input('[플레이어] 가위0,바위1,보2 : '))
            q8 = Quiz08Rps(player)
            print(f"가위 바위 보 의 결과는 : {q8.game()}")
# --------------------------------------------------------------
        elif menu == '9':
            q13 = Quiz09GetPrime()
# --------------------------------------------------------------
        elif menu == '10':
            year = int(input('년도입력 : '))
            q10 = Quiz10LeapYear(year)
            print(f"윤년확인 : {q10.leap()}")
# --------------------------------------------------------------
        elif menu == '11':
            q13 = Quiz11NumberGolf()
# --------------------------------------------------------------
        elif menu =='12':
            q12 = Quiz12Lotto()
            print(f"Lotto값 : {q12.lotto()}")
# -------------------------------------------------------------
        elif menu =='13':
            name = input('이름은: ')
            save = int(input('입금 : '))
            withdrawal = int(input('출금 : '))
            balance = 0;
            q13 = Quiz13Bank(name,save,withdrawal,balance)
            print(f'잔고는 {q13.balance}입니다.')
# --------------------------------------------------------------
        elif menu =='14':
            q14 = Quiz14Gugudan()
            print(f"구구단 : {q14.gugudan()}")
# --------------------------------------------------------------