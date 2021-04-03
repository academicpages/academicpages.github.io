from requests import get
from bs4 import BeautifulSoup
from googlesearch import search

url = 'https://aistats.org/aistats2021/accepted.html'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

x = html_soup.find_all('div', class_ = 'wrapper')

# print(x[1].li.b)
y = x[1].find_all('li')

for i in y:
    if 'priva' in i.b.text.lower():
        flag = False
        for j in search(i.b.text):
            if 'arxiv' in j:
                print(f'|[{i.b.text}]({j})||')
                flag = True
                break
            elif 'pdf' in j:
                print(f'|[{i.b.text}]({j})||')
                flag = True
                break
            else:
                continue
        if flag == False:
            print(f'|{i.b.text}||')

# |[A Simple and Practical Algorithm for Private Multivariate Mean and Covariance Estimation](https://arxiv.org/abs/2006.06618)||
