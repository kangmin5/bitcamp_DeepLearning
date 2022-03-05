import random


class Quiz10:

    def quiz10bubble(self) -> str:
        # 무작위 10까지 10개 뽑기
        arr = random.sample(range(10), 10)  # random.sample함수는 난수의 범위,갯수,중복이 제거된 것으로 나옴
        print(f'무작위 10개 값 : {arr}')
        # 버블정렬
        input('<누르면 버블정렬>')
        for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        print(f'버블 정렬 후 결과 : {arr}')

        return None

    # --------------------------------------------------------------------
    def quiz11insertion(self) -> str:
        # 무작위 10개 뽑기
        arr = random.sample(range(10), 10)
        print(f'무작위 10개 값 : {arr}')
        # 삽입 정렬
        input('<누르면 삽입정렬>')
        for i in range(len(arr)):
            temp = arr[i]
            j = i - 1
            while j >= 0 and arr[j] > temp:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = temp
        print(f'삽입 정렬 후 결과 : {arr}')

        return None

    # --------------------------------------------------------------------
    def quiz12selection(self) -> str:
        return None

    def quiz13quick(self) -> str:
        return None

    def quiz14merge(self) -> str:
        return None

    def quiz15magic(self) -> str:
        return None

    # ----------------------------------------------
    # 숫자를 지그재그로 출력하는 건가?
    #    행과 열을 input으로 입력 받고
    #    2중for문을 사욯한다. (첫번쨰 것이 행, 두번쨰것이 열)
    #    1씩 더해주고 출력되게 하고
    #
    #

    def quiz16zigzag(self) -> str:
        # n = int(input('행입력'))
        # m = int(input('열입력'))
        # cnt =1
        # for i in range(n):
        #     for j in range(m):
        #         print(cnt, end=' ')
        #         cnt += 1
        #     print()

        n = int(input('배열'))
        arr = [[0] * n for _ in range(n)]  # 배열을 0으로 n개의 행을 만드는 방법
        cnt = 1
        for i in range(len(arr)):  # 행
            if i % 2 == 0:  # 짝수번째 행이면(0,2,4~)
                for j in range(len(arr[i])):  # 열 정방향 출력 방식 arr[i]
                    arr[i][j] = cnt
                    cnt += 1
            elif i % 2 == 1:  # 홀수번째 행이면(1,3,5~)
                for j in range(len(arr[i]) - 1, -1, -1):  # 열 역방향 출력 뒤에 -1,-1,-1
                    arr[i][j] = cnt
                    cnt += 1

        for i in arr:
            print(f'{i}')

        return None

    # ------------------------------------------------------
    # 숫자를 정하면 2~ 숫자까지의 소수 구하기

    def quiz17prime(self) -> str:
        value = int(input('최대값 입력:'))
        res = ''
        for i in range(2, value):
            count = 0
            for j in range(2, i + 1):
                if i % j == 0:
                    count += 1
            if count == 1:
                res += str(i) + '\t'
        print(f'최대값{value}의 소수값 : {res}')
        return None

    # -----------------------------------------------------
    # 1~100 사이의 수 맞추기 (몇 번만에 찾는지 카운트 까징~)
    def quiz18golf(self) -> str:
        count = 0
        num = random.randint(1, 100)
        while 1:
            choice = int(input('숫자 선택(1~100) :'))
            count += 1;
            if choice > num:
                print(f'down')
            elif choice < num:
                print(f'up')
            elif choice == num:
                print(f'정답 {num} ,{count}번 만에 맟춤')
                break

        return None

    # -----------------------------------------------------------
    # 이건 뭐지? 예약프로그램인가 그건가?
    def quiz19booking(self) -> str:
        return None
