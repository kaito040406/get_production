import requests 
# HTTPにたいして、GETリクエストを出すために必要

import time
# サーバーの負荷を軽減させるため、処理を一時中断させるために必要

from bs4 import BeautifulSoup
# 取得したHTMLを解析するのに必要

from requests_html import HTMLSession
# リアルタイムの情報を取得するのに必要


# 取得したいページのURL
url = "https://www.amazon.co.jp/%E8%85%95%E6%99%82%E8%A8%88%E3%83%99%E3%83%AB%E3%83%88%E3%83%94%E3%83%B3-%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC-%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%94%E3%83%B3-%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC%E3%83%94%E3%83%B3%E3%83%AA%E3%83%A0%E3%83%BC%E3%83%90%E3%83%BC-18%E3%82%B5%E3%82%A4%E3%82%BA%EF%BC%888-25mm%EF%BC%89/dp/B07ZPSRS3R/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1583242817&sr=8-2"
session = HTMLSession()
r = session.get(url)

# d_soupにHTML全体の情報を格納
d_soup = BeautifulSoup(r.content, "html.parser")

# 取得したHTML全体の情報の中の　.a-column.a-span6.a-spacing-base.a-ws-span6　のクラス名を含む要素を取得
# 複数あるので、基本的に、配列で格納される
text = d_soup.select(".a-column.a-span6.a-spacing-base.a-ws-span6", recursive=False)

print(text)