import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
import unicodedata
import re
import csv
import json
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize 
from collections import defaultdict
import numpy as np
import calendar
from numpy import arange
import pylab as pl

base_url = "https://www.seek.com.au/jobs-in-information-communication-technology/engineering-software"
seed_url = base_url 

visited = {}; 
   
quotes=[]  # a list to store quotes 

visited[seed_url] = True

links = soup.findAll('a')
seed_link = soup.findAll('a', href=re.compile("^index.html"))
to_visit_relative = list(set(links) - set(seed_link))
to_visit_relative = [l for l in links if l not in seed_link]

to_visit = []
count = 0 
for link in to_visit_relative:
    count = count + 1;
    #print(count)
    if(count>=277 and count<=282):
        print(link['href'])