import requests
from bs4 import BeautifulSoup

url = 'http://xkcd.com'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'lxml').select('div a')
print('Verifying every linked page on the URL...')
for each in range(len(soup)):
    link = soup[each].get('href')
    if link.startswith('http'):
        url = link
    elif link.startswith('//'):
        url = 'http:' + link
    elif link.startswith('/'):
        url = 'http://xkcd.com' + link
    try:
        res = requests.get(url)
        res.raise_for_status()
    except Exception as err:
        print('Broken Link:', err)
