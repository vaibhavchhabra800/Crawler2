import requests
from lxml import html
import bs4

res = requests.get('https://www.codechef.com/ratings/all?order=asc&page=3&sortBy=global_rank', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'})
soup1=bs4.BeautifulSoup(res.text,'lxml')


print(res.text)

