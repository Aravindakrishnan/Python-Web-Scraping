from urllib.request import urlopen
from bs4 import BeautifulSoup
# website link -> https://appdevelopermagazine.com/Programming
import sqlite3
try:          
               page = urlopen("https://appdevelopermagazine.com/Programming")
except Exception as e:
               print(e)
soup = BeautifulSoup(page.read())

#scraping the data
title = soup.findAll('h2',{'class':'entry__title'}) #get the title title is <a> tag
content = soup.findAll('div',{'class':'entry__excerpt'}) # get the content
date = soup.findAll('span',{'class':'date-one'}) #get the date posted

#All the contents will be stored in the these lists

titles = []
contents = []
dates = []
links = []

#storing 
for t in title:
               titles.append(t.a.get_text())
for c in content:
               contents.append(c.a.get_text())
for d in date:
               dates.append(d.get_text())
for l in title:
               links.append(t.a.get('href'))
               
datastore = list(zip(titles,contents,dates,links))
print(datastore)
