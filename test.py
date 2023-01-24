import requests
from bs4 import BeautifulSoup
# import pandas as pd

def extract(page):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
    url = f'https://fr.indeed.com/jobs?q=data+analyst&l=Paris+%2875%29&start=(page)'
    r = requests.get(url, headers)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup
    

def transform(soup):
    divs = soup.find_all('div', class_ = 'jobseach')
    for item in divs:
        title = item.find('span', {'id' : 'jobTitle'}).text.strip()
        company = item.find('span', class_ = 'companyName').text.strip()
        # try:
        #     salary = item.find('span', class_ = 'salaryText').text.strip()
        # except:
        #     salary=''
        # summary = item.find('div', {'class' : 'summary'}).text.strip().replace('\n','')
        print(company)
    return
c = extract(0)
print(transform (c))




        # job = {
        #     'title': title, 
        #     'comapany': company,
        #     'salary': salary,
        #     'summary': summary
        # }
#         joblist.append(job)

# joblist = []

# for i in range(0, 40, 10):
     


# print(joblist)


# df = pd.DataFrame(joblist)
# print(df.head())
# df.to_csv('jobs.csv')
