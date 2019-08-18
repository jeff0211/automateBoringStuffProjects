import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

emailRecep = sys.argv[1]
emailMsg = ' '.join(sys.argv[2:])
if len(sys.argv) < 3:
    print('Please Enter myEmailer<space><Recipient email><space><Your Message>.')

else:
    """FOR INITIALISING GOOGLE CHROME AND LOADING MICROSOFT OUTLOOK HOMEPAGE"""
    browser = webdriver.Chrome()
    browser.implicitly_wait(1)
    browser.get('https://outlook.live.com')
    browser.find_element_by_link_text('Sign in').click()

    """FOR SIGNING IN EMAIL"""
    userNameElem = browser.find_element_by_id('i0116')
    userNameElem.send_keys('youremailadd@hotmail.com', Keys.ENTER)
    passwordElem = browser.find_element_by_id('i0118')
    passwordElem.send_keys('yourpassword')
    # Inspect element to find class="inline-block" for the 'Sign in' button, right click and copy its XPath for signInElem below.
    signInElem = browser.find_element_by_xpath('//*[@id="i0281"]/div/div/div[1]/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div')
    signInElem.click()

    """FOR CREATING AND SENDING NEW EMAIL MSG"""
    newMsgElem = browser.find_element_by_class_name('qtRcagoPZ5dw3xsr114ze')
    newMsgElem.click()
    RecepElem = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[3]/div['
                                              '1]/div/div/div/div[1]/div[1]/div[1]/div/div[1]/div/div/div/div/div['
                                              '1]/div/div/input')
    RecepElem.send_keys(emailRecep)
    TitleElem = browser.find_element_by_xpath('//*[@id="subjectLine0"]')
    TitleElem.send_keys('Automated Emailer')
    contentElem = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[3]/div['
                                                '1]/div/div/div/div[1]/div[2]/div')
    contentElem.send_keys(emailMsg)
    sendElem = browser.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[2]/div/div[3]/div[1]/div/div/div/div[1]/div[4]/div[2]/div[1]/button[1]/div')
    sendElem.click()
    print('Your email is sent to {}.'.format(emailRecep))





