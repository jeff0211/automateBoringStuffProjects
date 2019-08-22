import requests, re, os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

os.makedirs('imgDL', exist_ok=True)

"""SEARCHES FOR PHOTOS ON FLICKR"""
mySearch = input('Search for: ')
browser = webdriver.Chrome()
browser.get('https://www.flickr.com/')
browser.find_element_by_id('search-field').send_keys(mySearch, Keys.ENTER)

"""CREATING A LIST ON ALL ELEMENTS OF class='view photo-list-photo-view awake' WITHIN 'div' TAG"""
res = requests.get('https://www.flickr.com/search/?text=' + mySearch)
soup = BeautifulSoup(res.text, 'lxml')
searchElem = soup.select('div > .view.photo-list-photo-view.awake')
print('Search completed!')

"""DOWNLOAD SEARCH RESULTS"""
for each in range(len(searchElem)):
    imgSrc = searchElem[each].get('style')
    imgURL = 'https:' + re.search(r'\/\/.*.jpg', imgSrc).group()
    res = requests.get(imgURL)
    print('Downloading image ' + os.path.basename(imgURL))
    with open(os.path.join('imgDL', os.path.basename(imgURL)), 'wb') as imageFile:
        for chunk in res.iter_content(10000):
            imageFile.write(chunk)
browser.close()
print('Download Completed!')
