import selenium
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import re

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

driver = selenium.webdriver.Chrome(service=s, options=chrome_options)

#site opening
driver.get("https://www.vlr.gg/event/matches/1015/valorant-champions-2022/?series_id=2184")
time.sleep(1)


# Function to generate safe filenames from the page title
def generate_safe_filename(base_name, n, a_index):
    # Retrieve the page title
    page_title = driver.title

    # Sanitize the title to make it file-system safe
    sanitized_title = re.sub(r'[\\/*?:"<>|]', "", page_title).strip()

    # Format filename with base name, page title, and div/a indices
    filename = f"{sanitized_title}_div{n}_a{a_index}.html"

    return filename


# Function to extract elements, scroll, and save HTML content
def extract_elements_html_with_navigation_to_file(n_start, n_end):
    for n in range(n_start, n_end + 1, 2):  # Iterate over the changing div numbers

        try:
            # Dynamically count how many 'a' elements are present within the current 'div'
            div_xpath = f'//*[@id="wrapper"]/div[1]/div/div[{n}]'
            a_elements = driver.find_elements(By.XPATH, f"{div_xpath}/a")

            # If 'a' elements are found, iterate over them
            for a_index in range(1, len(a_elements) + 1):
              xpath = f'{div_xpath}/a[{a_index}]'  # Create the general XPath dynamically

              try:
                # Click the link to navigate to the new page
                driver.find_element(By.XPATH, xpath).click()
                time.sleep(3)  # Wait for the new page to load

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

                # Generate a safe filename using the sanitized page title
                filename = generate_safe_filename("page", n, a_index)

                # Save the specific HTML content to a file
                with open(filename, "w", encoding="utf-8") as f:
                    f.write(specific_section_html)
                # Navigate back to the previous page
                driver.back()
                time.sleep(8)  # Wait for the previous page to load

              except Exception as e:
                print(f"Element not found for {xpath}: {str(e)}")

        except Exception as e:
            print(f"Error processing div {n}: {str(e)}")

    # Optional sleep between iterations to avoid detection

time.sleep(1)


# Call the function to extract and save HTML content
extract_elements_html_with_navigation_to_file(14, 18)

#close the chrome browser
driver.quit()