class Calcurator():

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


class Grade():
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def sum(self):
        return self.kor + self.eng + self.math

    def avg(self):
        return (self.kor + self.eng + self.math) / 3


class Bmi(object):

    def __init__(self, name, height, weight):

        self.name = name
        self.height = height
        self.weight = weight

    def bmi(self):
        bmi = (weight / (height ** 2)) * 10000

        if bmi >= 30.0:
            return f'{bmi} 비만'
        elif 25.0 <= bmi < 30.0:
            return f'{bmi} 과체중'
        elif 18.5 <= bmi < 25.0:
            return f'{bmi} 정상'
        else:
            return f'{bmi} 저체중'

        return bmi


if __name__ == '__main__':
    while 1:
        menu = input('0.Exit 1.계산기(+-*/) 2.Bmi 3.Grade')
        if menu == 0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            opcode: str = input('연산자')
            num2 = int(input('두번째 수'))
            # 객체생성
            calc = Calcurator(num1, num2, opcode)
            if opcode == '+':
                result = calc.add()
            elif opcode == '-':
                result = calc.sub()
            elif opcode == '*':
                result = calc.mul()
            elif opcode == '/':
                result = calc.div()

            print('*' * 30)
            print(f'{calc.num1}{opcode}{calc.num2}={result}')
            print('*' * 30)

        elif menu == '2':
            name: str = input('이름 입력')
            height = float(input('키 입력'))
            weight = float(input('몸무게 입력'))

            bmi = Bmi(name, height, weight)
            print(f'{name}님의 키는{height}이고 몸무게는{weight}이고 BMI는 {bmi.bmi()}  입니다..')

        elif '3':
            name = input('이름 : ')
            kor = int(input('국어 : '))
            eng = int(input('영어 : '))
            math = int(input('수학 : '))
            grade = Grade(name, kor, eng, math)

            print(f'{name}님의 국어{kor} 영어{eng} 수학{math} 이고 합계는{grade.sum()} 이고 평균은{grade.avg()} 입니다.')
