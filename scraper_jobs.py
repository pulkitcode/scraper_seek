import requests 
from bs4 import BeautifulSoup 
import csv 

URL = "https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software"
r = requests.get(URL) 

soup = BeautifulSoup(r.content, 'html.parser') 
quotes=[]  # a list to store quotes 
table = soup.find('h1') 
print(table.text)

for row in table.findAll('div', 
                         attrs = {'data-search-sol-meta':'{"searchRequestToken":"241a0b2b-355b-461c-bd26-5a747d0ae416","jobId":"50566707";,"section";:"TOP","sectionRank":2,"jobAdType":"SPONSORED","tags":{"mordor:flights":"mordor_49","seek:innerWidth":"717","seek:innerHeight":"621","seek:customVersion":"9300","seek:page":"SERP"},"eventTime":1601380736420,"type":"ACTIVITY","activityType":"IMPRESSION"}'}): 
    print(row)
    quote = {} 
    quote['url'] = row.a['href'] 
    quotes.append(quote) 
filename = 'inspirational_quotes.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['url']) 
    w.writeheader() 
    for quote in quotes:
        print(quote)
        w.writerow(quote)
