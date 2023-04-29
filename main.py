from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.keys import Keys
import time

chrome_options = ChromeOptions()
chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("start-maximized")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("no-sandbox")
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("disable-blink-features=AutomationControlled")

service = Service(r"Path to your chromedriver_win32/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3529313271&distance=10&f_E=1%2C2&f_WT=2&geoId=101515487&keywords=data%20analyst%20apprenticeship&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

time.sleep(2)

sign_in = driver.find_element(By.XPATH, "/html/body/div[3]/header/nav/div/a[2]")
sign_in.click()

time.sleep(3)

email_input = driver.find_element(By.XPATH, '//*[@id="username"]')
email_input.send_keys("Your Email")

password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
password_input.send_keys("Your Password")

sign_in_button = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_button.click()

time.sleep(3)

all_jobs = driver.find_elements(By.CSS_SELECTOR, '.job-card-container--clickable')

for job in all_jobs:
    job.click()
    time.sleep(2)
    
    a = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button > span:nth-child(1)').get_attribute("textContent").strip()
    if a == "Save":
        save = driver.find_element(By.CSS_SELECTOR, '.jobs-save-button')
        save.click()
        time.sleep(1)
    else:
        pass

# To follow instead of save

#follow = driver.find_element(By.XPATH, '//*[@id="ember1414"]/section/div[1]/div[1]/button/svg')

#print(driver.find_element(By.XPATH, '//*[@id="ember1414"]/section/div[1]/div[1]/button/span').get_attribute("textContent").strip())
#if driver.find_element(By.XPATH, '//*[@id="ember159"]/section/div[1]/div[1]/button/span').get_attribute("textContent").strip() == "Follow":
     #follow.click()