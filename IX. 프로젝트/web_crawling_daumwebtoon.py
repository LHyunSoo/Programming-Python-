#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
from urllib.request import urlopen
import json

if __name__ == '__main__':
    # 다음 웹툰 > 굿바이 사돈 제목 가져오기
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/goodbyeinlaw") as data:
        j=json.loads(data.read())      # httpResponse -> json
    # print(j["data"]["webtoon"]["webtoonEpisodes"][1]["title"])

    html = "<html><head><meta charset='utf-8'></head><body>"
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]    #data.webtoon.webtoonEpisodes
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
        html+="<a href='{}'><img src='{}'/></a>",format(url.thumbnail, title)
    html += "</body></html>"

    outputSoup = BeautifulSoup(html, "lxml")  # 내가 생성한 html 문자열을 soup 객체로 만들기
    prettyHtml = str(outputSoup.prettify())

    with open("굿바이 사돈.html", "w", encoding="utf-8") as f:  # html 파일 만들기
        f.write(prettyHtml)