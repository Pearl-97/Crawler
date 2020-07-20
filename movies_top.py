# 引用requests库
import requests
# 引用BeautifulSoup库
from bs4 import BeautifulSoup

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Cache-Control': 'max-age=0',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36',
    'Connection': 'keep-alive',
    'Referer': 'http://www.baidu.com/'
}
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}

movies = open('movies.txt', 'a+')
for x in range(10):
    url = 'https://movie.douban.com/top250?start=' + str(x * 25) + '&filter='
    res = requests.get(url, headers=headers)
    bs = BeautifulSoup(res.text, 'html.parser')
    bs = bs.find('ol', class_="grid_view")
    for titles in bs.find_all('li'):
        # 查找序号
        num = titles.find('em', class_="").text
        # 查找电影名
        title = titles.find('span', class_="title").text
        # 查找推荐语
        tes = ''
        if titles.find('span', class_="inq"):
            tes = titles.find('span', class_="inq").text
        # 查找评分
        comment = titles.find('span', class_="rating_num").text
        # 查找链接
        url_movie = titles.find('a')['href']

        movie = num + '.' + title + '——' + comment + '\n' + '推荐语：' + tes + '\n' + url_movie + '\n'
        movies.write(movie)

movies.close()
