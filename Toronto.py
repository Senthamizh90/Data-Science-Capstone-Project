# This is Data Science Capstone Project
import pandas as pd
import numpy as np
print("Hello Capstone Project Course!")

''' from bs4 import BeautifulSoup
import requests
wiki_url="https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"

r=requests.get(wiki_url)
soup=BeautifulSoup(r.text,'html.parser')
ct=soup.find('table',class_ ='wikitable sortable')

df=pd.read_html(str(ct))

df1=df[df.Borough  != 'Not assigned'''

df1 = pd.read_csv('Toronto Data.csv')
