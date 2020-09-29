import requests 
from bs4 import BeautifulSoup 
import csv 
   
URL = "https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software"
r = requests.get(URL) 
   
soup = BeautifulSoup(r.content, 'html.parser') 
   
quotes=[]  # a list to store quotes 
   
table = soup.find('section', attrs = {'aria-label':'Search Results'})

#print(table)
   
for row in table.findAll('article', attrs = {'data-automation':'normalJob'}): 
    
    #print(row)
    quote = {} 
    quote['job_names'] = row.h1.text
    quotes.append(quote) 
   
#print(quotes)
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='\n') as f: 
    w = csv.DictWriter(f,['job_names']) 
    w.writeheader() 
    for quote in quotes: 
        w.writerow(quote)