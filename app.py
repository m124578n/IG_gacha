import requests
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as Soup
import time
# response = requests.get('https://www.instagram.com/p/C1RvNsLy0kb/')

browser = webdriver.Chrome()
url = 'https://www.instagram.com/p/C1RvNsLy0kb/'
browser.get(url)

# need loop to run to the down
element = browser.find_element(By.XPATH, '//*[@id="mount_0_0_N7"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]')
scroll = 'arguments[0].scrollTop = arguments[0].scrollHeight;'
browser.execute_script(scroll, element)

element = browser.find_elements(By.XPATH, '//*[@id="mount_0_0_N7"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]')

page_source = browser.page_source
soup = Soup(page_source, 'html.parser')


soup.find('div')
all_comments = soup.find_all(class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')
all_comments[1].find_all(class_='x9f619 xjbqb8w x78zum5 x168nmei x13lgxp2 x5pf9jr xo71vjh xsag5q8 xz9dl7a x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s x1q0g3np xqjyukv x1qjc9v5 x1oa3qoh x1nhvcw1')



all_messages = element[0].text
split_list = all_messages.split('\n')
all_split_messages = split_list[8:]
c = 0
all_list = []
temp_list = []
for x in all_split_messages:
    if c == 5:
        all_list.append(temp_list)
        c = 0
        temp_list = []
    else:
        temp_list.append(x)
        c += 1


'//*[@id="mount_0_0_N7"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]'
'//*[@id="mount_0_0_N7"]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/section/main/div/div[1]/div/div[2]/div/div[2]/div/div[2]/div[4]'
