import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import time
import pathlib
import os


def recusrsiveWorkingForA(recursive_key,N,driver,HTML_SAVING_DIR_LOC,match_url_link):
    
    if recursive_key == -1:
        return None
    
    else:
        
        try:
            driver.get(match_url_link)
            WebDriverWait(driver, 15)
            
            xpath = f'//*[@id="wrapper"]/div[1]/div/div[{N}]/a[{recursive_key}]'
            xpath = r'{}'.format(xpath)
            print(f"Checking Into Match with a = {recursive_key} with xpath:- {xpath}")
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, xpath)))
            driver.find_element(By.XPATH, xpath).click()
            
        except Exception as e:
            
            print(f"Cannot find the  xpath with a = {recursive_key} and xpath = {xpath} hence quiting and running for new N")
            return recusrsiveWorkingForA(recursive_key=-1,N=None,driver=None,HTML_SAVING_DIR_LOC=None,match_url_link=None)
        
        else:
            
            print(f"Into the a = {recursive_key}")
            target_xpath = '//*[@id="wrapper"]/div[1]/div[3]/div[6]/div/div[3]'
            WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, target_xpath)))

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
            
            
            files = os.listdir(HTML_SAVING_DIR_LOC)
            if len(files) == 0:
                file_number = 0
            else:
                file_number = sorted(files,key=lambda x: int(x[x.index("__")+2:x.rindex("__")]))[-1]
                file_number = int(file_number[file_number.index("__")+2:file_number.rindex("__")])
            OUTUPT_HTML_FILE_LOC = HTML_SAVING_DIR_LOC.joinpath(f"FILENO__{file_number+1}__708TECH.html")
            with open(OUTUPT_HTML_FILE_LOC, "w", encoding="utf-8") as f:
                    print(f"Saving File for a = {recursive_key} and xpath = {xpath}")
                    print(f"\nLocation :- {OUTUPT_HTML_FILE_LOC}")
                    f.write(specific_section_html)

            # Navigate back to the previous page
            # Wait for the previous page to load
            return recusrsiveWorkingForA(recursive_key=recursive_key+1,N=N,driver=driver,HTML_SAVING_DIR_LOC=HTML_SAVING_DIR_LOC,match_url_link=match_url_link)




def workingForN(hit_N,driver,HTML_SAVING_DIR_LOC,match_url_link):  
      
      
    went_wrong = True
    print("<---------------------------------->")
        
    try:

        driver.get(match_url_link)
        WebDriverWait(driver, 15)
        
        N_xpath = f'//*[@id="wrapper"]/div[1]/div/div[{hit_N}]/a[1]'
        N_xpath = r'{}'.format(N_xpath)
        
        print(f"Trying for N={hit_N} using N_xpath:- {N_xpath}")
        WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, N_xpath)))  
        driver.find_element(By.XPATH, N_xpath).click()
        
            
    except Exception as e:
            
        print(f"Excpetion Occrued for N = {hit_N} on N_xpath = {N_xpath}")
            
    else :
            
        print(f"Succesful Hit for N = {hit_N} and xpath = {N_xpath}\n Going For a Runs!!!")
        recusrsiveWorkingForA(recursive_key=1,N=hit_N,driver=driver,HTML_SAVING_DIR_LOC=HTML_SAVING_DIR_LOC,match_url_link=match_url_link)
        went_wrong = False 
        
    print(f"Done for N = {hit_N}")
    print("<---------------------------------->")
    return went_wrong
        
        
# Function to extract elements, scroll, and save HTML content
def extract_elements_html_with_navigation_to_file(HTML_SAVING_DIR_LOC,match_url_link,driver):
    
    wrong_hits = set()
    hit_N = 4
    while len(wrong_hits) <= 9:
        
        went_wrong = workingForN(hit_N=hit_N,driver=driver,HTML_SAVING_DIR_LOC=HTML_SAVING_DIR_LOC,match_url_link=match_url_link)
        
        if went_wrong == True:
            wrong_hits.add(hit_N)
        
        hit_N += 2
        
time.sleep(1)



def main(match_url_link,HTML_SAVING_DIR_LOC):
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])

    # to remove errors
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--ignore-ssl-errors")

    #maximize the browser
    chrome_options.add_argument("start-maximized")

    service = Service(ChromeDriverManager().install())
    driver = selenium.webdriver.Chrome(service=service, options=chrome_options)
    

    # Call the function to extract and save HTML content  
    
    extract_elements_html_with_navigation_to_file(HTML_SAVING_DIR_LOC=HTML_SAVING_DIR_LOC,match_url_link=match_url_link,driver=driver)
    
    #close the chrome browser
    driver.quit()
    
    
if __name__ == "__main__":
        
    match_url_link = r"https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=2184"
    main(match_url_link=match_url_link)
