import random


class Quiz20:

    def quiz20list(self) -> str: return None

    def quiz21tuple(self) -> str: return None

    def quiz22dict(self) -> str: return None
#--------------------------------------------------------------
    def quiz23listcom(self) -> str:
        print('-----------legacy-----------')
        a = []                                 # a = list() 와 같다.
        for i in range(5):
            a.append(i)
        print(a)
        print('--------comprehension----------')
        a2 = [i for i in range(5)]            # 이걸 사용해야 한다. (일 순위)  리스트 컴프리핸션 (list comprehension)
        print(a2)
        return None
#--------------------------------------------------------------
    def quiz24zip(self) -> str: return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27(self) -> str: return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None
