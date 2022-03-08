import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup


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
    def quiz24zip(self) -> str:
        url='https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser vs lxml
        print(soup.prettify())

        data = soup.find_all('p',{'class':'artist'})
        # print(type(data))  'bs4.element.ResultSet' 결과가 데이타셋의 class라서 리스트,튜플,딕셔너리중 하나로 내려야 함.
        data = [i for i in data]
        # print(type(data))
        data = [i.get_text() for i in data]
        print(''.join(i for i in data))
        # data = soup.select('.byChart>tbody>tr>td>p>a')
        # print(data)

        # data = soup.select_one('.byChart>tbody>tr>td>p>a').string
        # print(data)

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/63.0.3239.132 Safari/537.36'}
        url='https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req), 'lxml')  # html.parser vs lxml
        print(soup.prettify())
        data = soup.select('.wrap_song_info>.ellipsis>span>a')
        data = [i.get_text() for i in data]
        title =data[0::2]
        singer = data[1::2]
        for i,j in enumerate(title):print(f'{i+1}등 곡명:{j}')
        for x,y in enumerate(singer):print(f'{x+1}등 가수:{y}')




        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None
