from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
s = Service("C:/Users/ADITYA/OneDrive/Desktop/chromedriver.exe")

# set different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# to remove errors
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

#maximize the browser
chrome_options.add_argument("start-maximized")

driver = webdriver.Chrome(service=s, options=chrome_options)

#site opening
driver.get("https://www.google.co.uk/")
time.sleep(2)


a=driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
a.send_keys("liquepedia valorant")
a.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()
time.sleep(8)



driver.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div/div[2]/div/div[3]/div/div/a').click()
time.sleep(5)


driver.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div/div[1]/ul/li[2]/a').click()
time.sleep(4)

old_height= driver.execute_script("return document.body.scrollHeight")

while True:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(2)

    new_height = driver.execute_script("return document.body.scrollHeight")
    if old_height == new_height:
        break


    old_height=new_height

html= driver.page_source

with open ("team_list.html", "w") as f:
    f.write(html)

driver.quit()