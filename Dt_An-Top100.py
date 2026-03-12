import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url="https://www.billboard.com/charts/hot-100/"
page = requests.get(url)

info = BeautifulSoup(page.content, 'html.parser')
results = info.find_all('div', class_="o-chart-results-list-row-container")

with open("Billboard.csv",'w',newline='',encoding='utf8') as fh:
    w=csv.writer(fh)
    w.writerow(['Rank','Title',"Artists",'Weeks On'])
    
    for result in results:
        L=[]
        rank=result.find('span','c-label')
        ranks=rank.text.strip()
        L.append(ranks)
        
        title=result.find('h3','c-title')
        titles=title.text.strip()
        L.append(titles)
        
        
        artist=result.find('span',"c-label a-no-trucate a-font-secondary u-font-size-15 u-font-size-13@mobile-max u-line-height-18px@mobile-max u-letter-spacing-0010 u-line-height-21px a-children-link-color-black a-children-link-color-brand-secondary:hover lrv-a-children-link-decoration-underline:hover lrv-u-display-block a-truncate-ellipsis-2line u-max-width-397 u-max-width-230@tablet-only u-max-width-300@mobile-max")
        artists=artist.text.strip()
        L.append(artists)
        
        weeksr=result.find_all('span',"c-label u-font-family-secondary@mobile-max u-font-family-basic@tablet u-font-weight-800@tablet u-font-size-12 u-line-height-normal lrv-u-padding-tb-00@mobile-max u-min-width-30px u-width-auto@mobile-max u-min-width-auto@mobile-max lrv-u-margin-r-050@mobile-max")
        k=0
        for j in weeksr:
            weeks=j
            if(k==3):
                break
        weekss=weeks.text.strip()
        L.append(weekss)
        w.writerow(L)
    print("Done Making The CSV File \n")



df= pd.read_csv("Billboard.csv")
bar1=df['Artists'].value_counts()

plt.figure(figsize=(10,6))
bar1.plot(kind='bar', color='red', edgecolor='black')

plt.title('Frequency of Artists on The Billboard Hot 100')
plt.xlabel('Artists')
plt.ylabel('Number of Songs')
#plt.xticks(rotation=45, ha='right')

plt.show()

df.plot(x='Rank', y='Weeks On', kind='line', figsize=(32,20), marker='o', color='orange')
plt.title('Plot of Rank vs No.of weeks')
plt.grid(True)
plt.show()

print("Mean Number of Weeks a song stays on Billboard: ")
print(df['Weeks On'].mean())

print("Standard Deviation of the Number of Weeks a song stays on Billboard: ")
print(df['Weeks On'].std())

print("End of Code")
