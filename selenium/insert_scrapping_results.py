from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
service = Service(r'ChromeDriver\chromedriver.exe')
driver = webdriver.Chrome(service=service , options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://prestadom:80/admin996uxmty8/")

email = driver.find_element(By.ID, 'email')
email.send_keys("h0l0dn14ok@pepisandbox.com")#email
haslo = driver.find_element(By.ID, 'passwd')
haslo.send_keys("pasha1234567")#haslo

driver.find_element(By.ID, 'submit_login').click()
driver.find_element(By.CLASS_NAME, "mi-settings_applications").click()
driver.find_element(By.XPATH, "//li[@id='subtab-AdminImport']/a").click()


driver.find_element(By.XPATH, "//li[text()='file']").click()
pyautogui.write(r'C:\Users\Xotta\PycharmProjects\BE_scrapper\TEST.csv') #miejsce z cvs skrapowania
pyautogui.press('enter')



#do dokończenia




self.driver.quit();