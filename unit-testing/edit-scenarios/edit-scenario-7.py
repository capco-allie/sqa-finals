#  📌 Alice Nicole D. Capco 📌

# from pyvirtualdisplay import Display
from selenium import webdriver

# display = Display(visible=0, size=(1024, 768))
# display.start()

options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--headless')
options.add_argument('--incognito')
options.add_argument('--window-size=1920,1080')

driver = webdriver.Chrome(options=options)
driver.get("http://207.148.91.197:5000/")
driver.save_screenshot('scenario7/edit-scenario1.png') # 📌 Save screenshot code

driver.find_element_by_name('username').send_keys('maaagic')
driver.find_element_by_name('password').send_keys('maaagic')
driver.save_screenshot('scenario7/edit-scenario2.png')
driver.find_element_by_css_selector("[type='submit']").click()
driver.save_screenshot('scenario7/edit-scenario3.png')

toggle = driver.find_elements_by_class_name("dropdown-toggle")
toggle[1].click()
driver.save_screenshot('scenario7/edit-scenario4.png')

dropdown = driver.find_elements_by_class_name("dropdown-menu")
link = dropdown[1].find_elements_by_tag_name("a")
link[0].click()
driver.save_screenshot('scenario7/edit-scenario5.png')

lastname = driver.find_element_by_name('lastname')
lastname.clear()
driver.save_screenshot('scenario7/edit-scenario6.png')

firstname = driver.find_element_by_name('firstname')
firstname.clear()
driver.save_screenshot('scenario7/edit-scenario7.png')

birthdate = driver.find_element_by_name('birthdate')
birthdate.clear()
driver.save_screenshot('scenario7/edit-scenario8.png')

emailaddress = driver.find_element_by_name('emailaddress')
emailaddress.clear()
driver.save_screenshot('scenario7/edit-scenario9.png')

phonenumber = driver.find_element_by_name('phonenumber')
phonenumber.clear()
driver.save_screenshot('scenario7/edit-scenario10.png')

note = driver.find_element_by_name('note')
note.clear()
driver.save_screenshot('scenario7/edit-scenario11.png')

driver.find_element_by_id("add-contact-btn").click()
driver.save_screenshot('scenario7/edit-scenario12.png')

driver.quit()
# display.sendstop()
