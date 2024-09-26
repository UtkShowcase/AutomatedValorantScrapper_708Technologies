from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


def main(HTML_OUTPUT_LOC):
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # to remove errors
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    #maximize the browser
    chrome_options.add_argument("start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.get("https://www.google.co.uk/")
    WebDriverWait(driver, 7)

    a = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
    a.send_keys("liquepedia valorant")
    a.send_keys(Keys.ENTER)
    WebDriverWait(driver, 7)
    
    WebDriverWait(driver, 7).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3')))
    driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a/h3').click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="mw-content-text"]/div/div[2]/div/div[3]/div/div/a' ))) 
    driver.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div/div[2]/div/div[3]/div/div/a').click()

    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,r'//*[@id="mw-content-text"]/div/div[1]/ul/li[2]/a'))) 
    driver.find_element(by=By.XPATH, value='//*[@id="mw-content-text"]/div/div[1]/ul/li[2]/a').click()


    old_height= driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        time.sleep(2)

        new_height = driver.execute_script("return document.body.scrollHeight")
        if old_height == new_height:
            break


        old_height=new_height

    html= driver.page_source
    
    with open (HTML_OUTPUT_LOC, "w") as f:
        f.write(html)

    driver.quit()
