import time
import threading
import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from configparser import ConfigParser
import cv2
import pytesseract
import re
import numpy as np
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
        self.url = 'https://row4.vfsglobal.com/NetherlandsAppointment/Account/RegisteredLogin?q=shSA0YnE4pLF9Xzwon/x/GAZMwphNakm2hstnNbT9MeeIMxQ284VVU8CmQHTuVDj6RdcTCMqElpit5BM4ux0VE1qp9briBHUp2f3a3FAZaU='

        self.browser = uc.Chrome(options=self.options, driver_executable_path=os.path.join(driver_path,'chromedriver'))
        password = 'darrey327739'
        email = 'daretimileyin1@gmail.com'
        self.sign_in(email,password)
        
    def get_started(self):
        try:
          self.browser.get((self.url))
          WebDriverWait(self.browser, 600).until(EC.presence_of_element_located((By.CLASS_NAME, 'renderer-content')))
          #WebDriverWait(self.browser, 600).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/div/h2')))
          self.browser.find_element(by=By.PARTIAL_LINK_TEXT, value='Book now').click()
          print(self.browser.title)
          print(self.browser.current_url)
          WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div/div/main/div/div/div[2]/div/h2')))
          if 'Book an appointment' in self.browser.page_source:
              self.book_appointment()
          else:
              print("Book an appointment not in page source")
        except Exception as arr:
            print(arr)
            
            
    def book_appointment(self):
        try: 
           self.browser.delete_all_cookies()
           print(self.browser.title)
           print(self.browser.current_url)
           #self.browser.set_page_load_timeout(60)
           self.browser.find_element(by=By.PARTIAL_LINK_TEXT, value='Book now').click()
           #self.browser.set_page_load_timeout(50)
           #//*[@id="challenge-stage"]/div/label/input
           try:
               #self.browser.execute_script(f"window.open({self.browser.current_url}, '_blank');")
               #new_window = self.browser.window_handles[1]  
               #self.browser.switch_to.window(new_window)
               time.sleep(10)
               WebDriverWait(self.browser, 60).until(EC.visibility_of_any_elements_located((By.ID, 'challenge-stager')))
            #//*[@id="challenge-stage"]/div/label/span[1]
            #mark
            
               #self.browser.find_element(by=By.XPATH, value='//*[@id="challenge-stage"]').click()  
           except:
               print("element not located in the page")
           print("50 secs time")
           
           time.sleep(30)
          #//*[@id="EmailId"]
           password = 'darrey327739'
           email = 'daretimileyin1@gmail.com'
           self.sign_in(email,password)
           
        except RuntimeError:
            print("hello")
        except Exception as arr:
            #print(arr)
            print(arr)
        
        
        
    def sign_in(self,email, password):
       while True:   
         try:
             
             #WebDriverWait(self.browser, 600).until(EC.presence_of_element_located((By.NAME, 'EmailId')))
             time.sleep(1)
             print("signing in please wait...")           
             self.browser.find_element(by=By.ID, value='EmailId').send_keys(email)
             print("email input filled")
             time.sleep(2)
             self.browser.find_element(by=By.ID, value='Password').send_keys(password)
             print("password input filled")
             self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
             #driver.maximize_window()
             time.sleep(20)
             try:
                captcha_img = self.browser.find_element(by=By.ID, value='CaptchaImage')
                self.captcha_filename = 'captcha.png'
                with open(self.captcha_filename, 'wb') as file:
                    file.write(captcha_img.screenshot_as_png)
        
                captcha = self.break_captcha()
                
                self.browser.find_element(by=By.NAME, value='CaptchaInputText').send_keys(captcha)
             except:
                 time.sleep(15)
        
             
             time.sleep(1)
             self.browser.find_element(by=By.ID, value='btnSubmit').click()
             break
         except Exception as arr:
             self.browser.refresh()
             
    def break_captcha(self):
        image = cv2.imread("captcha.png")
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[250])
        image = cv2.filter2D(image, -1, np.ones((4, 4), np.float32) / 16)
    
        se = cv2.getStructuringElement(cv2.MORPH_RECT, (8,8))
        bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
        image = cv2.divide(image, bg, scale=255)
        image = cv2.filter2D(image, -1, np.ones((3, 4), np.float32) / 12)
        image = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]
    
        image = cv2.copyMakeBorder(image, 5, 5, 5, 5, cv2.BORDER_CONSTANT, value=[250])
    
        captcha = pytesseract.image_to_string(image, config='--psm 13 -c tessedit_char_whitelist=ABCDEFGHIJKLMNPQRSTUVWYZ')
        denoised_captcha =  re.sub('[\W_]+', '', captcha).strip()
    
        return denoised_captcha
    
        
       # #update.message.reply_text("Sending Captcha...")
#
       # captcha_img = self.browser.find_element(by=By.ID, value='CaptchaImage')
       # 
       # self.captcha_filename = 'captcha.png'
       # with open(self.captcha_filename, 'wb') as file:
       #     file.write(captcha_img.screenshot_as_png)

        #captcha = break_captcha()
        
        #self.browser.find_element(by=By.NAME, value='CaptchaInputText').send_keys(captcha)
        #time.sleep(10)
        #self.browser.find_element(by=By.ID, value='btnSubmit').click()
        
        
app = VFS_France()
    