import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time


service = Service(ChromeDriverManager().install())


# set different options for the browser
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

# to remove errors
chrome_options.add_argument("--ignore-certificate-errors")
chrome_options.add_argument("--ignore-ssl-errors")

#maximize the browser
chrome_options.add_argument("start-maximized")

driver = selenium.webdriver.Chrome(service=service, options=chrome_options)

#site opening
driver.get("https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=2184")
time.sleep(1)


'''def recursive_work(recursive_key,n):
    """_summary_

    Args:
        recursive_key (_type_): _description_

    Returns:
        _type_: _description_
    """
    
    
    if recursive_key == -1:
        return None 
    
    
    else:
        try:
            xpath = f'//*[@id="wrapper"]/div[1]/div/div[{n}]/a[{recursive_key}]'
            driver.find_element(By.XPATH, xpath).click()
            recursive_key += 1
            time.sleep(3)
                
        except Exception as e:
            xpath = f'//*[@id="wrapper"]/div[1]/div/div[{n}]/a]'
            driver.find_element(By.XPATH, xpath).click()
            recursive_key = -1
            time.sleep(3)

                # Wait for the target content section to be present
        target_xpath = '//*[@id="wrapper"]/div[1]/div[3]/div[6]/div/div[3]'
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, target_xpath)))

                # Find the scrollable section
        scrollable_element = driver.find_element(By.XPATH, target_xpath)
        last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

                    # Scroll within the specific section
        while True:
                    # Scroll down within the specific section
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

                    # Wait for the content to load
            time.sleep(2)

                    # Calculate new scroll height and compare with the last scroll height
            new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

            if new_height == last_height:
                    break  # Exit the loop if no new content is loaded

            last_height = new_height

                    # After scrolling, get the HTML content of the specific section
            specific_section_html = scrollable_element.get_attribute('outerHTML')

                    # Save the specific HTML content to a file
            
            filename = f"page_{n}_a{recursive_key}.html" if recursive_key != -1 else f"page_{n}_a.html"
            with open(filename, "w", encoding="utf-8") as f:
                    f.write(specific_section_html)

                    # Navigate back to the previous page
            driver.back()
            time.sleep(8)
            print(f"ended {recursive_key}")
        return recursive_work(recursive_key=recursive_key,n=n)'''


# Function to extract elements, scroll, and save HTML content
def extract_elements_html_with_navigation_to_file(n_start, n_end):
    for n in range(n_start, n_end + 1, 2):  # Iterate over the changing div numbers
        for a_index in range(1,3):
            double_match_fg = True
            try:
                print(f"Entered Try:- {a_index}")
                xpath = f'//*[@id="wrapper"]/div[1]/div/div[{n}]/a[{a_index}]'
                xpath = r'{}'.format(xpath)
                print(xpath)
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(3)
                print("going without error")
                
            except Exception as e:
                
                print(e)
                print("Entered Except")
                xpath = f'//*[@id="wrapper"]/div[1]/div/div[{n}]/a]'
                xpath = r'{}'.format(xpath)
                driver.find_element(By.XPATH, xpath).click()
                double_match_fg = False
                time.sleep(3)
                target_xpath = '//*[@id="wrapper"]/div[1]/div[3]/div[6]/div/div[3]'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, target_xpath)))

                # Find the scrollable section
                scrollable_element = driver.find_element(By.XPATH, target_xpath)
                last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

                    # Scroll within the specific section
                while True:
                    # Scroll down within the specific section
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

                    # Wait for the content to load
                    time.sleep(2)

                    # Calculate new scroll height and compare with the last scroll height
                    new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

                    if new_height == last_height:
                        break  # Exit the loop if no new content is loaded

                    last_height = new_height

                    # After scrolling, get the HTML content of the specific section
                    specific_section_html = scrollable_element.get_attribute('outerHTML')

                    # Save the specific HTML content to a file
                    filename = f"page_{n}_a{a_index}.html"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(specific_section_html)

                    # Navigate back to the previous page
                    driver.back()
                    time.sleep(8)
                    
                    a_index = 3
                
            else:
                
                # Wait for the target content section to be present
                target_xpath = '//*[@id="wrapper"]/div[1]/div[3]/div[6]/div/div[3]'
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, target_xpath)))

                    # Find the scrollable section
                scrollable_element = driver.find_element(By.XPATH, target_xpath)
                last_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

                        # Scroll within the specific section
                while True:
                        # Scroll down within the specific section
                    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrollable_element)

                        # Wait for the content to load
                    time.sleep(2)

                        # Calculate new scroll height and compare with the last scroll height
                    new_height = driver.execute_script("return arguments[0].scrollHeight", scrollable_element)

                    if new_height == last_height:
                        break  # Exit the loop if no new content is loaded

                    last_height = new_height

                        # After scrolling, get the HTML content of the specific section
                    specific_section_html = scrollable_element.get_attribute('outerHTML')

                        # Save the specific HTML content to a file
                    filename = f"page_{n}_a{a_index}.html"
                    with open(filename, "w", encoding="utf-8") as f:
                        f.write(specific_section_html)

                        # Navigate back to the previous page
                    driver.back()
                    time.sleep(8)
                    
                # Wait for the previous page to loa

  
    # Optional sleep between iterations to avoid detection

time.sleep(1)


# Call the function to extract and save HTML content
extract_elements_html_with_navigation_to_file(14, 18)

#close the chrome browser
driver.quit()