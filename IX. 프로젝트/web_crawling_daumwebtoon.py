#pip install beautifulsoup4
#pip install lxml

from urllib.request import urlopen
import json

if __name__ == '__main__':
    # 다음 웹툰 > 굿바이 사돈 제목 가져오기
    with urlopen("http://webtoon.daum.net/data/pc/webtoon/view/goodbyeinlaw") as data:
        j=json.loads(data.read())      # httpResponse -> json
    # print(j["data"]["webtoon"]["webtoonEpisodes"][1]["title"])
    cartoon_titles = j["data"]["webtoon"]["webtoonEpisodes"]    #data.webtoon.webtoonEpisodes
    for cartoon_title in cartoon_titles:
        title = cartoon_title["title"]
        print(title)
        thumbnail = cartoon_title["thumbnailImage"]["url"]
        print(thumbnail)
        url = cartoon_title["id"]
        url = "http://webtoon.daum.net/webtoon/viewer/"+str(url)
        print(url)