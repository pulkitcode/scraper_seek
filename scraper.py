import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html.parser') 
   
quotes=[]  # a list to store quotes 
   
table = soup.find('section', attrs = {'aria-label':'Search Results'})

#print(table)
   
for row in table.findAll('div', 
                         attrs = {'class':'_3MPUOLE'}): 
    
    print(row)
    quote = {} 
    quote['url'] = row.a['href'] 
 
    quotes.append(quote) 
   
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['url']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)