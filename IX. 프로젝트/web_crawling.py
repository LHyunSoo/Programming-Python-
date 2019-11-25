#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen

if __name__ == '__main__':
    #네이버 웹툰 > 연애혁명 제목 가져오기
    data = urlopen("https://comic.naver.com/webtoon/list.nhn?titleId=570503&weekday=thu")
    soup = BeautifulSoup(data,"lxml")
    #print(soup)
    cartoon_titles = soup.find_all("td",attrs={"class":"title"})
    for cartoon_title in cartoon_titles:
        title = cartoon_title.find("a").text
        print(title)