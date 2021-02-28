import urllib.request as request
import bs4

src = "https://www.baidu.com"
with request.urlopen(src) as response:
    data = response.read(15).decode('utf-8')
print(data)

# root = bs4.BeautifulSoup(data, "html.parser")
# titles = root.find("div", class_="index_left")
# for i in titles:
#     if titles.a != None:
#         print(titles.a)
