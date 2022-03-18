from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.common.keys import Keys

chromedriver_parth = "/home/suraj/Downloads/chromedriver"

options = webdriver.ChromeOptions()
s = Service(chromedriver_parth)
driver = webdriver.Chrome(service=s, options=options)
driver.get("https://en.wikipedia.org/wiki/Main_Page")
value = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
print(value.text)

# driver.find_element(by=By.LINK_TEXT, value="Science").click()
input = driver.find_element(by=By.NAME, value="search")
input.send_keys("I am a QA engineer")
input.send_keys(Keys.ENTER)



# driver.quit()