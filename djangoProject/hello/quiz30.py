import random
import string

import pandas as pd
from icecream import ic
import numpy as np

from context.models import Model
from hello.domains import myRandom, members

'''
    데이터프레임 문제 Q02
ic| df:     A   B   C
        1   1   2   3
        2   4   5   6
        3   7   8   9
        4  10  11  12
'''


class Quiz30:

    def quiz30_df_4_by_3(self) -> object:
        # 위 식을 리스트결합 형태로 분해해서 조립하시오
        # 1안
        col = list(string.ascii_uppercase)[:3]
        l = [[i + j for j in range(3)] for i in range(1, 13, 3)]
        df = pd.DataFrame(l, index=range(1, 5), columns=col)
        ic(df)
        # 2안
        l = [[i + j for i in range(4)] for j in range(1, 13, 3)]
        ls = [i for i in l]
        print(ls)
        z = dict(zip(col, ls))
        print(z)
        df2 = pd.DataFrame.from_dict(z)
        ic(df2)
        return None

    '''
        데이터프레임 문제 Q03.
        두자리 정수를 랜덤으로 2행 3열 데이터프레임을 생성
        ic| df:     0   1   2
                0  97  57  52
                1  56  83  80
    '''

    def quiz31_rand_2_by_3(self) -> str:
        li = [[random.randint(10, 99) for i in range(3)] for j in range(2)]
        # idx = list(range(2))
        # col = list(range(3))
        df = pd.DataFrame(li)
        ic(df)
        return None

    '''
            데이터프레임 문제 Q04.
            국어, 영어, 수학, 사회 4과목을 시험치른 10명의 학생들의 성적표 작성.
             단 점수 0 ~ 100이고 학생은 랜덤 알파벳 5자리 ID 로 표기

              ic| df4:        국어  영어  수학  사회
                        lDZid  57  90  55  24
                        Rnvtg  12  66  43  11
                        ljfJt  80  33  89  10
                        ZJaje  31  28  37  34
                        OnhcI  15  28  89  19
                        claDN  69  41  66  74
                        LYawb  65  16  13  20
                        QDBCw  44  32   8  29
                        PZOTP  94  78  79  96
                        GOJKU  62  17  75  49
    '''

    @staticmethod
    def id(char_size) -> str:
        return "".join(random.choice(string.ascii_letters) for i in range(char_size))

    def quiz32_df_grade(self) -> str:
        subjects = ['국어', '영어', '수학', '사회']
        score = np.random.randint(0, 100, (10, 4))
        idx = ["".join(random.choice(string.ascii_uppercase) for i in range(5)) for j in range(10)]
        df1 = pd.DataFrame(score, index=idx, columns=subjects)
        ic(df1)
        d = dict(zip(idx, score))
        df2 = pd.DataFrame.from_dict(d, orient='index', columns=subjects)
        ic(df2)

        return None

    @staticmethod
    def createDf(keys, vals, len):
        return pd.DataFrame([dict(zip(keys, vals)) for _ in range(len)])

    def quiz33_df_loc(self) -> str:
        # df = self.createDf(keys=['a', 'b', 'c', 'd'],
        #                    vals=np.random.randint(0, 100, 4),
        #                    len=3
        #                    )
        # ic(df)
        # ic(df.iloc[0])
        # ic(df.iloc[lambda x: x.index % 2 == 0])

        # kdt5기 수강생 성적 예제 프로그램
        # subjects = ['자바', '파이썬', '자바스크립트', 'SQL']
        # student = list(members())
        # d = [[random.randint(0,100) for i in range(4)] for j in range(len(student)) ]
        # dd = dict(zip(student,d))
        # df= pd.DataFrame.from_dict(dd,orient='index',columns=subjects)
        # ic(df)
        # 수강생 성적 리스트 END

        # 수강생 성적 랜덤으로 csv출력함
        #df.to_csv('./save/grade1.csv', sep=',', na_rep='NaN')
        # 출력 END

        # model = Model()
        # grade_df = model.new_model('grade.csv')

        # ic(grade_df)

        df = pd.read_csv('./save/grade1.csv', index_col=0)

        # print('01 파이썬의 columns 전체의 점수를 출력하시오.')
        # ic(df.loc[:,'파이썬'])
        print('02 조현국의 row를 출력하시오')
        ic(type(df.loc['조현국']))
        ic(df.loc['조현국'])
        print('03 강민의 자바 점수만 출력')
        ic(df.loc['강 민','자바'])
        print('04 자바스크립트 점수가 60점 이상인 list 뽑기')
        test=df['자바스크립트']>=60
        ic(df.loc[test])
        print('05 몇명 슬라이스')
        ic(df.loc['권솔이':'한성수'])
        # python_scores = None
        #
        # ic(python_scores)
        # ic(cho_scores)




        return None




    def quiz34_df_iloc(self) -> str: return None

    def quiz35(self) -> str: return None

    def quiz36(self) -> str: return None

    def quiz37(self) -> str: return None

    def quiz38(self) -> str: return None

    def quiz39(self) -> str: return None
