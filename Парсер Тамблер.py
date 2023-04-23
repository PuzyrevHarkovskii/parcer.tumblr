import os
import urllib.request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


url = 'https://3rd-world-elite.tumblr.com/'


if not os.path.exists('images'):
    os.makedirs('images')

driver = webdriver.Chrome()


driver.get(url)


while True:
    body = driver.find_element(By.XPATH, '//body')
    body.send_keys(Keys.PAGE_DOWN)
    images = body.find_elements(By.TAG_NAME, 'img')
    if len(images) >= 1000:  # Проверяем, что загружено достаточное количество изображений
        break

        
for image in images:
    src = image.get_attribute('src')
    if src.endswith('.jpg') or src.endswith('.png'):
        filename = src.split('/')[-1]
        filepath = os.path.join('images', filename)
        urllib.request.urlretrieve(src, filepath)
        print(f"Downloaded {filename}")

driver.quit()
