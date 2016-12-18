# Author  : George Poulos
# Version : 1.0
#
# Scraper for amazon products
#   This scraper grabs the data from the newer 'Product Information' table
#

from bs4 import BeautifulSoup
import requests

url = 'https://www.amazon.com/gp/product/B007CCKEEG/ref=s9_cartx_gw_g21_i3_r?ie=UTF8&fpl=fresh&pf_rd_m=ATVPDKIKX0DER&pf_rd_s=&pf_rd_r=GZHMCKZT8QHKD8CP683G&pf_rd_t=36701&pf_rd_p=b13ec477-194d-4f63-971b-ca6229de96a2&pf_rd_i=desktop'
response = requests.get(url, headers={'User-agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36'})

soup = BeautifulSoup(response.content)
tags = {}
divs = soup.select('table#productDetails_detailBullets_sections1 tr')
for li in divs:
    try:
        title = li.th
        key = title.text.strip().rstrip(':')
        value = title.next_sibling.strip()
        tags[key] = value
        body = li.td
        key = body.text.strip().rstrip(':')
        value = body.next_sibling.strip()
        tags[key] = value
    except AttributeError:
        break

for t in tags:
    print "{0}".format(t)