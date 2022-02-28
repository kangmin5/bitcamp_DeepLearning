class Calcurator(object):

    def __init__(self, num1, num2,opcode):
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


if __name__ == '__main__':

    while 1:
        menu = input('0.Exit 1.계산기(+-*/)')
        if menu == 0:
            break
        elif menu == '1':
            num1 = int(input('첫번째 수'))
            opcode = input('연산자')
            num2 = int(input('두번째 수'))
            # 객체생성
            calc = Calcurator(num1,num2,opcode)

            if(opcode == '+'):
                print('*' * 30)
                print(f'{calc.num1}+{calc.num2}={calc.add()}')
                print('*' * 30)
            elif(opcode == '-'):
                print('*' * 30)
                print(f'{calc.num1}-{calc.num2}={calc.sub()}')
                print('*' * 30)
            elif(opcode == '*'):
                print('*' * 30)
                print(f'{calc.num1}*{calc.num2}={calc.mul()}')
                print('*' * 30)
            elif(opcode == '/'):
                print('*' * 30)
                print(f'{calc.num1}/{calc.num2}={calc.div()}')
                print('*' * 30)