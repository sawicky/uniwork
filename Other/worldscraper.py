from string import ascii_letters, punctuation, whitespace
import requests, time, re
from bs4 import BeautifulSoup
from urllib import urlopen
import pandas as pd
ignore = ascii_letters + punctuation + whitespace

url = 'http://oldschool.runescape.com/c=sn10L0LBNoo/slu'
html = urlopen(url)
soup = BeautifulSoup(html, 'lxml')
player = soup.find_all('p', class_="player-count")
playerStr = str(player)
count = re.sub("[^0-9]", "", playerStr)
print(count)
worldsList = [a.getText() for a in soup.findAll('tr', limit=2)[1].findAll('a')]
worlds = ''.join(worldsList)
worldPopList = [td.getText() for td in soup.findAll('tr', limit=2)[1].findAll('td')]
print(worlds.replace("Old School ", "")), worldPopList[1]
data_rows = soup.findAll('tr')[1:]
type(data_rows)
server_data = [[td.getText() for td in data_rows[i].findAll('td')]
               for i in range(len(data_rows))]
plist = str(server_data)
plistsub = re.sub(r"[^0-9]", " ", plist)
plistsub2 = ' '.join(plistsub.split())
plistsub3 = plistsub2.split()
worldList_ = plistsub3[::2]
playerList_ = plistsub3[1::2]
d = dict(players = playerList_, world = worldList_)
finalList = pd.DataFrame({k : pd.Series(v) for k, v in d.iteritems()})
x = 1
while True:
    print finalList
    time.sleep(5)
    x+=1

