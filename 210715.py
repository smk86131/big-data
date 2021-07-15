# import pandas as pd
#
# dict_data = {'a' : 1, 'b' : 2, 'c' : 3}
# sr = pd.Series(dict_data)
# print(sr)
# print(sr['b'])
# import pandas as pd
#
# data = ('나겸','2021-07-13','여',False)
# sr = pd.Series(data, index=['이름','생년월일','성별','학생여부'])
# print(sr)
# import pandas as pd
#
# dict_data = {'c0' : [1,2,3], 'c1' : [4,5,6], 'c2' : [7,8,9], 'c3' : [10,11,12], 'c4' : [13,14,15]}
# df = pd.DataFrame(dict_data)
# print(type(df))
# print('\n')
# print(df)
# import pandas as pd
# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
#                   index=['준서', '예은'],
#                   columns=['나이', '성별', '학교'])
# print(df)
# print(df.index)
# print(df.columns)
# import pandas as pd
#
# df=pd.DataFrame([[15,'남','덕영중'],[17,'여','수리중']],
#                 index=['준서','예은'],
#                 columns=['나이','성별','학교'])
#
# df.rename(columns={'나이':'연령','성별':'남녀','학교':'소속'},inplace=True)
# df.rename(index={'준서':'학생','예은':'학생2'},inplace=True)
# print(df)
# import pandas as pd
#
# exam_data={'수학':[90,80,70],'영어':[98,89,95],
#            '음악':[85,95,100],'체육':[100,90,90]}
#
# df=pd.DataFrame(exam_data,index=['서준','우현','인아'])
# print(df)
# print('\n')
#
# #행삭제
# df2=df[:]
# df2.drop('우현',inplace=True)
# print(df2)
# print('\n')
#
# df3=df[:]
# df3.drop(['우현','인아'],axis=0,inplace=True)
# print(df3)
# print('\n')
#
# #열삭제
# df4=df[:]
# df4.drop('수학',axis=1,inplace=True)
# print(df4)
# print('\n')
#
# df5=df[:]
# df5.drop(['인아'],axis=0,inplace=True)
# df5.drop(['수학','체육'],axis=1,inplace=True)
# print(df5

import requests
from bs4 import BeautifulSoup
import pandas as pd


req = requests.get('http://media.daum.net/ranking/popular/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
newstitle = soup.select('a.link_txt')
newscomname = soup.select('.info_news')

lst1 = []
lst2 = []

for i in range(len(newscomname)):
    lst1.append(newscomname[i].text.strip())
    lst2.append(newstitle[i].text.strip())

result_file = pd.DataFrame({'newstitle':lst2, 'newscomname':lst1})
result_file.to_csv("C:\\Users\\KB\\Documents\\R\\result.csv", index=False,
                   encoding='euc-kr')
# utf-8, cp-949

