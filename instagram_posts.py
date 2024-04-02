
"""
Created By *Abdullah EL-Yamany*
-------------------------------
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, urllib.request

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.instagram.com/")

time.sleep(2)

# -------- Login ------- #
while True:
    try:
        username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        break
    except:
        time.sleep(3)

username.clear()
password.clear()

username.send_keys("xxxxxxxxxxxx") # Write Email or Phone
password.send_keys("xxxxxxxxxxxx") # Write Password

time.sleep(1)
login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#save your login info?
while True:
    time.sleep(5)
    try:
        notnow = driver.find_element(By.XPATH, '//div[@class="_ac8f"]/div[@role="button"]').click()
        break
    except:
        continue


#turn on notif
time.sleep(2)
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

name_search = "xxxxxxxxxxxx" # Write Username Of Account

url = f"https://www.instagram.com/{name_search}/"

time.sleep(3)
driver.get(url)
time.sleep(10)


#scroll
scrolldown=driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")
match=False
posts = []
while(match==False):
    last_count = scrolldown
    time.sleep(3)
    scrolldown = driver.execute_script("window.scrollTo(0, document.body.scrollHeight);var scrolldown=document.body.scrollHeight;return scrolldown;")

    links = driver.find_elements(By.TAG_NAME, "a")
    for link in links:
        try:
            post = link.get_attribute('href')
        except:
            continue
        if post not in posts:
            if '/p/' in post:
                posts.append(post)


    if last_count==scrolldown:
        match=True


imgs_link = []
number = 1

#get videos and images
download_url = ''
for post in posts:
    driver.get(post)
    shortcode = driver.current_url.split('/')[-2]
    num = 1
    time.sleep(3)

    main_div = driver.find_element(By.CSS_SELECTOR, 'div[class="x6s0dn4 x1dqoszc xu3j5b3 xm81vs4 x78zum5 x1iyjqo2 x1tjbqro"]')

    while True:
        imgs = main_div.find_elements(By.CSS_SELECTOR, "img[style='object-fit: cover;']")
        for img in imgs:
            link = img.get_attribute('src')
            if link not in imgs_link:
                urllib.request.urlretrieve(link, f'img_{number}{shortcode}{num}.jpg')
                num += 1
                imgs_link.append(link)

                time.sleep(5)

        try:
            driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]').click()
            time.sleep(3)
        except:
            number += 1
            break
