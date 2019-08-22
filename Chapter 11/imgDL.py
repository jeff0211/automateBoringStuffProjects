import requests, re, os
from bs4 import BeautifulSoup

"""
SEARCH FOR PHOTOS ON FLICKR & CREATING A LIST ON ALL ELEMENTS OF
class='view photo-list-photo-view awake' WITHIN 'div' TAG
"""
mySearch = input('Search for: ')
res = requests.get('https://www.flickr.com/search/?text=' + mySearch)
soup = BeautifulSoup(res.text, 'lxml')
searchElem = soup.select('div > .view.photo-list-photo-view.awake')
print('Search completed!')

"""DOWNLOAD SEARCH RESULTS"""
os.makedirs('imgDL', exist_ok=True)
for each in range(len(searchElem)):
    imgSrc = searchElem[each].get('style')
    imgURL = 'https:' + re.search(r'\/\/.*.jpg', imgSrc).group()
    res = requests.get(imgURL)
    print('Downloading image ' + os.path.basename(imgURL))
    with open(os.path.join('imgDL', os.path.basename(imgURL)), 'wb') as imageFile:
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
print('Download Completed!')
