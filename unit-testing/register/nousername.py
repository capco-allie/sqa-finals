from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome("C:/chromedriver_win32/chromedriver.exe")
driver.get('http://localhost:5000/login')
driver.save_screenshot('home.jpeg')
register = driver.find_element_by_css_selector("a.btn-outline-primary")
register.click()

driver.save_screenshot('signup.jpeg')

password = driver.find_element_by_name("password")
password.clear()
password.send_keys("demopassword")
driver.save_screenshot('filledpass.jpeg')
password.send_keys(Keys.RETURN)
driver.save_screenshot('nousername.jpeg')
driver.implicitly_wait(20)

# made by: Jessica Garay