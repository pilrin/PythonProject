import requests
from bs4 import BeautifulSoup

url = 'http://music.bugs.co.kr/chart'
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, 'html.parser')
music_list = soup.find_all('p', class_='title')
artist_list = soup.find_all('p', class_='artist')

for idx, title in enumerate(music_list):
    print(idx+1, end=' ')
    print(title.text.strip(), end='-')
    print(artist_list[idx].find_all('a')[0].text.strip())
