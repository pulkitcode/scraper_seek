import requests 
from bs4 import BeautifulSoup 
import csv 
   
#initialise the url 
URL = "https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software"
r = requests.get(URL) 
   
#create the parser object
soup = BeautifulSoup(r.content, 'html.parser') 
   
quotes=[]  #store quotes 
   

table = soup.find('section', attrs = {'aria-label':'Search Results'})

#print(table)
   
for row in table.findAll('article', attrs = {'data-automation':'normalJob'}): 
    
    #print(row)
    quote = {} 
    quote['job_names'] = row.h1.text
    quotes.append(quote) 
   
#print(quotes)
filename = 'inspirational_quotes.csv'
with open(filename, 'w') as f: 
    w = csv.DictWriter(f,['job_names']) 
    w.writeheader() 
    for quote in quotes: 
        print(quote)
        w.writerow(quote)
