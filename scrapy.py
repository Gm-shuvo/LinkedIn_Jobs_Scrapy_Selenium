import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
 
options = Options()
# options.add_argument('--headless')
# options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)




driver.get('https://www.linkedin.com/home')


mail = 'devilshuvo12@gmail.com'
password = 'devil91?'
driver.find_element(By.XPATH, "(//input[@type='text'])").send_keys(mail)
driver.find_element(
    By.XPATH, "(//input[@type='password'])").send_keys(password)
time.sleep(5)
driver.close()

