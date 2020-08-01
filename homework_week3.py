import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbsparta


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# 아래 빈 칸('')을 채워보세요
url = 'https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713](https://www.genie.co.kr/chart/top200?ditc=D&rtm=N&ymd=20200713'
data = requests.get(url,headers=headers)
soup = BeautifulSoup(data.text,'html.parser')


tables = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for x in tables:
    title = x.select_one('td.info > a.albumtitle.ellipsis').text.strip()
    rank = x.select_one('td.number').text[0:2].strip()
    artist = x.select_one('td.info > a.artist.ellipsis').text.strip()
    print(rank, title, artist)
    doc = {
        'rank': rank,
        'title': title,
        'artist': artist
    }
    db.musicchart.insert_one(doc)


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.title.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.number
#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis
#body-content > div.newest-list > div > table > tbody > tr:nth-child(2) > td.info > a.artist.ellipsis