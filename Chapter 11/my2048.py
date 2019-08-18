from selenium import webdriver
from selenium.webdriver.common.keys import Keys

"""FOR INITIALISING GOOGLE CHROME AND 2048 WEB PAGE"""
browser = webdriver.Chrome()
browser.get('https://gabrielecirulli.github.io/2048/')

"""FOR PLAYING THE GAME 2048 (INFINITE LOOP)"""
while True:
    try:
        playElem = browser.find_element_by_tag_name('html')
        playElem.send_keys(Keys.UP, Keys.RIGHT, Keys.DOWN, Keys.LEFT)
        browser.find_element_by_class_name('retry-button').click()
    except:
        continue






