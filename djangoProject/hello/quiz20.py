import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

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
    @staticmethod
    def find_music(soup,data) -> []:
        ls = soup.find_all('p', {'class': data})
        return [i.get_text() for i in ls]

    @staticmethod
    def dict1(ls1,ls2)->None:
        dict = {}
        for i in range(0, len(ls1)):
            dict[ls1[i]] = ls2[i]    #중요,중요(리스트를 키와 value로 만드는 공식
        print(dict)

    @staticmethod
    def dict2(ls1,ls2)->None:
        dict = {}
        for i, j in enumerate(ls1):
            dict[j] = ls2[i]        ## 핵심,핵심 i는 인덱스로 j는 value
        print(dict)

    def quiz24zip(self) -> {}:
        url='https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml')
        ls1 = self.find_music(soup, 'title')
        ls2 = self.find_music(soup, 'artist')
        dict={}
        for i, j in zip(ls1,ls2):
            dict[i] = j               ### 이것이 결론 (이걸 써라....최신)zip : 리스트를 딕셔너리로 합치는 것
        print(dict)
        return dict
        # self.dict1(ls1,ls2)
        # self.dict2(ls1,ls2)


        # print(soup.prettify())
        # for i,j in enumerate(['artist','title']):
        #     for i,j in enumerate([self.find_music(soup,j)]):
        #         print(f'{i}위 : {j}')
        # data = soup.find_all('p',{'class':'artist'})
        # print(type(data))  'bs4.element.ResultSet' 결과가 데이타셋의 class라서 리스트,튜플,딕셔너리중 하나로 내려야 함.
        # data = [i for i in data]
        # print(type(data))
        # data1 = soup.find_all('p',{'class':'title'})
        # data1 = [i.get_text() for i in data1]
        # print(''.join(i for i in data1))
        # data = soup.select('.byChart>tbody>tr>td>p>a')
        # print(data)
        # data = soup.select_one('.byChart>tbody>tr>td>p>a').string
        # print(data)

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None
#---------------------------------------------------------------------
    @staticmethod
    def find_melon(soup,data) -> []:
        ls = soup.select(data)
        return [i.get_text() for i in ls]

    def quiz27melon(self) -> {}:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36'}
        url='https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')  # html.parser vs lxml
        # print(soup.prettify())
        ls1 = self.find_melon(soup, '.wrap_song_info>.ellipsis>span>a')
        title =ls1[0::2]
        singer = ls1[1::2]
        dict={}
        for i,j in zip(title,singer):
            dict[i] = j
        print(dict)
        return dict

    def quiz28dataframe(self) -> str:
        #dict = self.quiz24zip()
        # df = pd.DataFrame.from_dict(dict, orient='index')
        # print(df)
        # df.to_csv('./save/bugs.csv',sep=',',na_rep='NaN')

        dict = self.quiz27melon()
        df = pd.DataFrame.from_dict(dict,orient='index')
        print(df)
        df.to_csv('./save/melon.csv',sep=',',na_rep='NaN')

        return None

    def quiz29(self) -> str: return None
