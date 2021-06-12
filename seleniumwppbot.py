from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import itertools
import pandas as pd
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

#open driver and load configuration
url = 'https://web.whatsapp.com/'
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir=C:\\Users\\Farz\\AppData\\Local\\Google\\Chrome\\User Data')
driver = webdriver.Chrome(chrome_options=options, executable_path=r'C:\python\extention\chromedriver.exe')
driver.get(url)
wait = WebDriverWait(driver, 60)
print(f"{bcolors.OKGREEN}Chrome opened sucessfully!{bcolors.ENDC}")
driver.get(url)
print(f"{bcolors.OKGREEN}Accessing Whatsapp web{bcolors.ENDC}")

#find menssage/contacts
df = pd.read_excel('C:\\Users\\Farz\\Desktop\\contacts.xlsx')
Menssage = df['Menssage'].tolist()
Name = df['Name'].tolist()
print(f'{bcolors.OKGREEN}Contacts and menssage loaded with successful{bcolors.ENDC}')

#sending menssagem
for i, j in zip(Menssage, Name):
    Search = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div/div[1]/div[1]/div[3]/div/div[1]/div/label/div/div[2]")))
    time.sleep(1)
    Search.send_keys(j)#NUMBER
    time.sleep(1)
    Search.send_keys(Keys.ENTER)
    time.sleep(1)
    Menssage = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')[0]
    time.sleep(1)
    Menssage.send_keys(f'Hi, {j}')
    time.sleep(1)
    Menssage.send_keys(Keys.ENTER)#MENSSAGE
    time.sleep(1)
    Menssage.send_keys(i)
    time.sleep(1)
    Menssage.send_keys(Keys.ENTER)
    print(f'{bcolors.OKGREEN}Mensagem enviado para:{bcolors.ENDC} {bcolors.WARNING}{j}{bcolors.ENDC}')
