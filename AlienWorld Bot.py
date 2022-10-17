import time
from selenium import webdriver
import selenium
import imaplib
import smtplib
import email
import re
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import JavascriptException, TimeoutException
from imaplib import IMAP4


import random

import os
import json
from time import sleep
import os

os.chdir(os.path.dirname(os.path.abspath(__file__))) # Current Working Directionary 



driver = webdriver.Chrome(executable_path="") #chromedriver path

driver.maximize_window()

driver.get("https://alienworlds.io/?locale=de")


#Login in Page

ButtonLoginAlienWorld = driver.find_elements_by_xpath("//*[@class='css-3vja5m e1wmhysh3']")
while(ButtonLoginAlienWorld == None):
   time.sleep(1)
   ButtonLoginAlienWorld = driver.find_elements_by_xpath("//*[@class='css-3vja5m e1wmhysh3']")
main_window_handle = None
while not main_window_handle:
    time.sleep(1)
    main_window_handle = driver.current_window_handle
ButtonLoginAlienWorld[0].click()


#Recognize Popup and login to wallet

#Popup 1 waiting
Approve_Wax_Wallet_Popup_Window = None
while not Approve_Wax_Wallet_Popup_Window:
    time.sleep(1)
    for handle in driver.window_handles:
        if handle != main_window_handle:
            Approve_Wax_Wallet_Popup_Window = handle
            break


time.sleep(2.4)

#Popup 2 waiting
Signin_Ailenworlds_Popup_Window = None
while not Signin_Ailenworlds_Popup_Window:
    time.sleep(1)
    for handle in driver.window_handles:
        if handle != main_window_handle and handle != Approve_Wax_Wallet_Popup_Window:
            Signin_Ailenworlds_Popup_Window = handle
            break


driver.switch_to.window(Signin_Ailenworlds_Popup_Window)

#Human Behavior
rand = random.uniform(2.4, 5)
time.sleep(rand)

email = ""
pw = ""
#Popup waiting if usernameInputField is loaded then everything else for login is loaded!
UsernameInputfield = None
while(UsernameInputfield == None):
   time.sleep(1)
   UsernameInputfield = driver.find_element_by_name("userName")

#Login

#Human Behavior for typing in e-mail
#I know it's irrelevant in an html docuemt but that makes the variability accurate
#2.5 - 8 letters per second
for s in email:
    a = random.uniform(0.125, 0.4)
    time.sleep(a)
    driver.find_element_by_name("userName").send_keys(s)

#Human Behavior for typing in pw 
for s in pw:
    a = random.uniform(0.125, 0.4)
    time.sleep(a)
    driver.find_element_by_name("password").send_keys(s)

#Human Behavior
rand = random.uniform(0.5, 2)
time.sleep(rand)
driver.find_elements_by_xpath("//*[@class='button-primary full-width button-large text-1-5rem text-bold']")[0].click()

#wait for email
#imap
time.sleep(60)
while(True):
 try:
    mail=imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login('','') # "email address", "password"
    mail.list()
    mail.select('inbox')

    result, data = mail.search(None, "ALL")
 
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
 
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
 
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads

    m = re.findall(">([0-9]{6})<", str(raw_email)) #RegEx to extract the confirmation code
    print(m)
 except mail.abort:
    continue

 break
    

    



driver.find_element_by_name("code").send_keys(m)
rand = random.uniform(0.5, 2)
time.sleep(rand)
driver.find_elements_by_xpath("//*[@class='button primary']")[0].click()
time.sleep(10)

driver.switch_to.window(Approve_Wax_Wallet_Popup_Window)
rand = random.uniform(0.5, 2)
time.sleep(rand)
#New popup to approve so we have to wait for it to load, The buttons seem to have the same class names but on different pages!
BtnApprove = None
while(BtnApprove == None):
   time.sleep(1)
   BtnApprove = driver.find_elements_by_xpath("//*[@class='button button-secondary button-large text-1-5rem text-bold mx-1']")

#Human Behavior
rand = random.uniform(1, 3)
time.sleep(rand)
driver.find_elements_by_xpath("//*[@class='button button-secondary button-large text-1-5rem text-bold mx-1']")[0].click()

driver.switch_to.window(main_window_handle)

i = 1
#Mine 100 times
while(i < 100):
 #Human Behavior and you have to wait 5 seconds to mine after login!
 rand = random.uniform(10, 15)
 time.sleep(rand)


 #Find the Mine Button
 BtnMine = None
 while(BtnMine == None):
   BtnMine = driver.find_elements_by_xpath("//*[@class='css-10opl2l e1wmhysh2']")

 driver.find_elements_by_xpath("//*[@class='css-10opl2l e1wmhysh2']")[0].click()

 #Human Behavior and you have to wait some seconds to claim your reward after mining!
 rand = random.uniform(5, 7)
 time.sleep(rand)


 #Find the Mine Button
 BtnClaim = None
 while(BtnMine == None):
    time.sleep(1)
    BtnMine = driver.find_elements_by_xpath("//*[@class='css-1knsxs2 e1wmhysh2']")

 driver.find_elements_by_xpath("//*[@class='css-1knsxs2 e1wmhysh2']")[0].click()

 Approve_Wax_Wallet_Popup_Window2 = None
 while not Approve_Wax_Wallet_Popup_Window2:
     time.sleep(1)
     for handle in driver.window_handles:
         if handle != main_window_handle:
            Approve_Wax_Wallet_Popup_Window2 = handle
            break


 driver.switch_to.window(Approve_Wax_Wallet_Popup_Window2)
 BtnApprove = None
 while(BtnApprove == None):
   time.sleep(1)
   BtnApprove = driver.find_elements_by_xpath("//*[@class='button button-secondary button-large text-1-5rem text-bold mx-1']")

 #Human Behavior
 rand = random.uniform(5, 8)
 time.sleep(rand)
 driver.find_elements_by_xpath("//*[@class='button button-secondary button-large text-1-5rem text-bold mx-1']")[0].click()

 driver.switch_to.window(main_window_handle)
 i += 1
 time.sleep(180) #mining power for my Nft was every 180 seconds
