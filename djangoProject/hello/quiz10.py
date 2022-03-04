import random


class Quiz10:

    def quiz10bubble(self) -> str: return None

    def quiz11insertion(self) -> str: return None

    def quiz12selection(self) -> str: return None

    def quiz13quick(self) -> str: return None

    def quiz14merge(self) -> str: return None

    def quiz15magic(self) -> str: return None

    def quiz16zigzag(self) -> str: return None

# ------------------------------------------------------
    def quiz17prime(self) -> str:
        value = int(input('최대값 입력:'))
        res = ''
        for i in range(2,value):
            count =0
            for j in range(2,i+1):
                if i % j == 0:
                    count +=1
            if count == 1:
                res += str(i) + '\t'
        print(f'최대값{value}의 소수값 : {res}')
        return None
# -----------------------------------------------------
    def quiz18golf(self) -> str: return None

    def quiz19booking(self) -> str: return None