#---------- Create by Kauan Leandro ----------

#importing needed libraries
from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys
import time

#open google and go to whatsapp web site
driver = wd.Chrome('chromedriver.exe')
driver.get('https://web.whatsapp.com')
time.sleep(10)

contacts = str(["put the name of the contact/group exactly as it is saved on your cell phone, if you don't, it may cause an error"])
message = str('put the message you want to send')

#look for contacts
def searchContacts(contacts):
    searchXpath = '//*[@id="side"]/div[1]/div/label/div/div[2]'
    searchBox = driver.find_element_by_xpath(searchXpath)
    searchBox.send_keys(contacts)
    time.sleep(1.5)
    searchBox.send_keys(Keys.ENTER)

#send the messages
def sendMessage(menssage):
    messageXpath = '//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]'
    messageBox = driver.find_element_by_xpath(messageXpath)
    messageBox.send_keys(message)
    time.sleep(1)
    messageBox.send_keys(Keys.ENTER)

#send the message to all names on the list
for i in contacts:
    searchContacts(i)
    sendMessage(message)