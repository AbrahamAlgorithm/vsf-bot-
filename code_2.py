import time
import threading
import undetected_chromedriver as uc
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import os 
file = os.path.dirname(__file__)
driver_path = os.path.join(file,'chromedriver-linux64')
chrome_path = os.path.join(file,'chrome-linux64')
#from webdriver_manager.chrome import ChromeDriverManager


class VFS_France:
    def __init__(self):
        self.options = uc.ChromeOptions()
        self.options.add_argument("--no-sandbox")
        self.options.add_argument("--disable-dev-shm-usage")
        self.options.add_argument('--disable-gpu')
        self.options.add_argument("--disable-popup-blocking")
        self.options.add_argument("--disable-javascript")
        self.options.add_argument("disable-infobars")
        self.options.add_argument("--incognito")
        self.url = 'https://visa.vfsglobal.com/ind/en/pol/login'
        
        self.browser = uc.Chrome(options=self.options, driver_executable_path=os.path.join(driver_path,'chromedriver'))
    def sign_in(self,email, password):
       while True:   
         try:
             self.browser.delete_all_cookies()
             self.browser.get(self.url)
             WebDriverWait(self.browser, 60).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'ng-star-inserted')))
             time.sleep(15)
             email = 'daretimileyin1@gmail.com'
             password = '@Darrey327739'
                          
             self.browser.find_element(by=By.XPATH, value='//*[@id="mat-input-0"]').send_keys(email)
             print("email input filled")
             time.sleep(2)
             self.browser.find_element(by=By.XPATH, value='//*[@id="mat-input-1"]').send_keys(password)
             print("password input filled")
             self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             #driver.maximize_window()
             time.sleep(20)
             
             button =self.browser.find_element(by=By.XPATH,value='/html/body/app-root/div/div/app-login/section/div/div/mat-card/form/button')
             time.sleep(3)
             button.click()
             break
         except Exception as arr:
             self.browser.refresh()
             
    def apply_button(self):
        WebDriverWait(self.browser, 60).until(EC.visibility_of_any_elements_located((By.CLASS_NAME, 'mat-tab-labels')))
        button =self.browser.find_element(by=By.XPATH,value='/html/body/app-root/div/div/app-dashboard/section[1]/div/div[2]/div/button')
        time.sleep(3)
        button.click()
        
    def book_appointment(self,application_center,application_category, application_sub_category):
        #/html/body/app-root/div/div/app-eligibility-criteria/section/form
        WebDriverWait(self.browser, 60).until(EC.visibility_of_element_located((By.XPATH, '/html/body/app-root/div/div/app-eligibility-criteria/section/form')))
        value1 = Select(self.browser.find_element(by=By.XPATH, value='//*[@id="mat-select-0"]'))
        time.sleep(1)
        value1.select_by_value(application_center)
        time.sleep(1)  #
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        value1 = Select(self.browser.find_element(by=By.XPATH, value='//*[@id="mat-select-4"]'))
        time.sleep(1)
        value1.select_by_value(application_category)
        time.sleep(1)
        value1 = Select(self.browser.find_element(by=By.XPATH, value='//*[@id="mat-select-2"]'))
        time.sleep(1)
        value1.select_by_value(application_sub_category)
        time.sleep(3)
        if "We are sorry but no appointment slots are currently available. New slots open at regular intervals, please try again later" in self.browser.page_source:
            pass
    def close(self):
        self.browser.quit()
        
        
               
if __name__ =='__main__':        
   app = VFS_France()
   email = 'daretimileyin1@gmail.com'
   password = '@Darrey327739'
   app.sign_in(email, password)
   print("successfully login!")
   time.sleep(2)
   app.apply_button()
   time.sleep(3)
   app.close()