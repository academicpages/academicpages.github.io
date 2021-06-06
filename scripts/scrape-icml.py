from requests import get
from bs4 import BeautifulSoup
from googlesearch import search


url = 'https://icml.cc/Conferences/2021/AcceptedPapersInitial'
response = get(url)

html_soup = BeautifulSoup(response.text, 'html.parser')

x = html_soup.find_all('div', class_ = 'col-xs-9')

print(x[1].find_all('p')[2].b)
# print(x[1].p.b.text.lower())
# y = x[1].find_all('li')
y = x[1].find_all('p')[2:]
for i in y:
    if ('priva' in i.b.text.lower()) or ('federated' in i.b.text.lower()):
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

# # |[A Simple and Practical Algorithm for Private Multivariate Mean and Covariance Estimation](https://arxiv.org/abs/2006.06618)||